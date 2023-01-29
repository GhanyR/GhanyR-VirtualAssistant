# from pydub import AudioSegment
import os
os.environ["PATH"] += os.pathsep + "C:/Python310/ffmpeg/bin"

import subprocess

# Mempercepat audio menjadi 2 kali lipat
subprocess.run(["ffmpeg", "-i", "original.mp3", "-filter:a", "atempo=2.0", "-vn", "faster.mp3"])
