#!/usr/bin/env python3
"""
Smart Second Brain - Dual-Engine Voice Cloning Tool
Supports VOXCPM2 and MiMo VoiceClone
Optimized for Chinese speech
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path
import requests

# Configuration
CONFIG = {
    "voxcomm2": {
        "api_url": "https://api.voxcomm2.com/tts",
        "api_key": os.getenv("VOXCOMM2_API_KEY", ""),
        "model": "voxcomm2-chinese"
    },
    "mimo": {
        "api_url": "https://api.moonshot.cn/v1/audio/speech",
        "api_key": os.getenv("MIMO_API_KEY", ""),
        "model": "moonshot-v1-tts"
    },
    "output_dir": "output/voice",
    "temp_dir": "temp/voice",
    "normalize_audio": True,
    "target_loudness": -16  # LUFS
}

def check_ffmpeg():
    """Check if ffmpeg is installed"""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ffmpeg not found. Please install ffmpeg first.")
        print("   Windows: choco install ffmpeg")
        print("   Mac: brew install ffmpeg")
        print("   Linux: sudo apt install ffmpeg")
        return False

def normalize_audio(input_path, output_path):
    """Normalize audio using ffmpeg loudnorm filter"""
    if not CONFIG["normalize_audio"]:
        return input_path
    
    cmd = [
        "ffmpeg", "-i", input_path,
        "-af", f"loudnorm=I={CONFIG['target_loudness']}:TP=-1.5:LRA=11",
        output_path, "-y"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✅ Audio normalized: {output_path}")
            return output_path
        else:
            print(f"  ⚠️  Audio normalization failed: {result.stderr}")
            return input_path
    except Exception as e:
        print(f"  ⚠️  Audio normalization error: {e}")
        return input_path

def generate_speech_voxcomm2(text, output_path, reference_audio=None):
    """Generate speech using VOXCPM2"""
    config = CONFIG["voxcomm2"]
    
    if not config["api_key"]:
        print("❌ VOXCPM2 API key not found. Set VOXCOMM2_API_KEY environment variable.")
        return None
    
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": config["model"],
        "input": text,
        "voice": "chinese-female",
        "response_format": "mp3"
    }
    
    if reference_audio:
        # Upload reference audio for voice cloning
        with open(reference_audio, "rb") as f:
            files = {"audio": f}
            response = requests.post(f"{config['api_url']}/clone", headers=headers, files=files, json=payload)
    else:
        response = requests.post(config["api_url"], headers=headers, json=payload)
    
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"  ✅ Generated (VOXCPM2): {output_path}")
        return output_path
    else:
        print(f"  ❌ VOXCPM2 API error: {response.status_code} - {response.text}")
        return None

def generate_speech_mimo(text, output_path, reference_audio=None):
    """Generate speech using MiMo VoiceClone"""
    config = CONFIG["mimo"]
    
    if not config["api_key"]:
        print("❌ MiMo API key not found. Set MIMO_API_KEY environment variable.")
        return None
    
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": config["model"],
        "input": text,
        "voice": "chinese-female",
        "response_format": "mp3"
    }
    
    if reference_audio:
        # MiMo uses reference audio for voice cloning
        payload["reference_audio"] = reference_audio
    
    response = requests.post(config["api_url"], headers=headers, json=payload)
    
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"  ✅ Generated (MiMo): {output_path}")
        return output_path
    else:
        print(f"  ❌ MiMo API error: {response.status_code} - {response.text}")
        return None

def generate_voice_clone(text, output_path, engine="mimo", reference_audio=None):
    """Generate voice clone using specified engine"""
    print(f"🎤 Generating voice clone ({engine})...")
    print(f"  Text: {text[:50]}...")
    
    # Create output directory
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Generate speech
    if engine == "voxcomm2":
        result = generate_speech_voxcomm2(text, output_path, reference_audio)
    elif engine == "mimo":
        result = generate_speech_mimo(text, output_path, reference_audio)
    else:
        print(f"❌ Unknown engine: {engine}")
        return None
    
    if not result:
        return None
    
    # Normalize audio
    if CONFIG["normalize_audio"]:
        normalized_path = str(Path(output_path).with_suffix(".normalized.mp3"))
        result = normalize_audio(output_path, normalized_path)
    
    print(f"✅ Voice clone generated: {result}")
    return result

def batch_generate(texts, output_dir, engine="mimo", reference_audio=None):
    """Batch generate voice clones"""
    print(f"📦 Batch generating {len(texts)} voice clones...")
    
    results = []
    for i, text in enumerate(texts):
        output_path = Path(output_dir) / f"voice_{i:03d}.mp3"
        result = generate_voice_clone(text, str(output_path), engine, reference_audio)
        if result:
            results.append(result)
    
    print(f"✅ Batch generation complete: {len(results)} files")
    return results

def merge_audio_files(audio_files, output_path):
    """Merge multiple audio files into one"""
    print(f"🔄 Merging {len(audio_files)} audio files...")
    
    # Create file list for ffmpeg
    list_file = Path(CONFIG["temp_dir"]) / "file_list.txt"
    list_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(list_file, "w", encoding="utf-8") as f:
        for audio_file in audio_files:
            f.write(f"file '{Path(audio_file).absolute()}'\n")
    
    # Merge using ffmpeg
    cmd = [
        "ffmpeg", "-f", "concat", "-safe", "0",
        "-i", str(list_file),
        "-c", "copy", output_path, "-y"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✅ Audio merged: {output_path}")
            return output_path
        else:
            print(f"  ❌ Audio merge failed: {result.stderr}")
            return None
    except Exception as e:
        print(f"  ❌ Audio merge error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Dual-Engine Voice Cloning Tool")
    parser.add_argument("--text", help="Text to generate speech")
    parser.add_argument("--text-file", help="Text file containing text")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--engine", default="mimo", choices=["voxcomm2", "mimo"], help="Engine to use")
    parser.add_argument("--reference-audio", help="Reference audio for voice cloning")
    parser.add_argument("--batch", action="store_true", help="Batch mode")
    parser.add_argument("--merge", help="Merge audio files into one")
    
    args = parser.parse_args()
    
    print("🎤 Dual-Engine Voice Cloning Tool")
    print("=" * 50)
    
    # Check ffmpeg
    if not check_ffmpeg():
        return
    
    if args.merge:
        # Merge mode
        audio_files = args.merge.split(",")
        output_path = args.output or "output/voice/merged.mp3"
        merge_audio_files(audio_files, output_path)
        
    elif args.batch:
        # Batch mode
        if not args.text_file:
            print("❌ --text-file required for batch mode")
            return
        
        with open(args.text_file, "r", encoding="utf-8") as f:
            texts = [line.strip() for line in f if line.strip()]
        
        output_dir = args.output or CONFIG["output_dir"]
        batch_generate(texts, output_dir, args.engine, args.reference_audio)
        
    else:
        # Single mode
        if not args.text:
            print("❌ --text required for single mode")
            return
        
        output_path = args.output or "output/voice/output.mp3"
        generate_voice_clone(args.text, output_path, args.engine, args.reference_audio)
    
    print("\n" + "=" * 50)
    print("✅ Voice cloning complete!")

if __name__ == "__main__":
    main()
