# audio2numpy
[![Build Status](https://travis-ci.com/wiccy46/audio2numpy.svg?branch=master)](https://travis-ci.com/wiccy46/audio2numpy)

## Description

audio2numpy load an audio file and directly ouputs the audio data as a numpy array and its sampling rate. Supports .wav, .aiff via python's standard library, and .mp3 via ffmpeg.

## Installation

Using pip:

    pip install audio2numpy

## FFmpeg for decoding mp3
audio2numpy requires ffmpeg to decode mp3 files. You would need to install ffmpeg in order to have mp3 support. 

### macOS
    homebrew install ffmpeg

### Linux
    sudo apt-get install ffmpeg
[Check here](https://www.ostechnix.com/install-ffmpeg-linux/) for other installation methods for different Linux distributions. 

### Windows
- Download the latest distribution from https://ffmpeg.zeranoe.com/builds/
- Unzip the folder, preferably to `C:\`
- Append the FFmpeg binary folder (e.g. `C:\ffmpeg\bin`) to the PATH system variable ([How do I set or change the PATH system variable?](https://www.java.com/en/download/help/path.xml))

## Usage

    from audio2numpy import open_audio
    fp = "./examples/word.mp3"  # change to the correct path to your file accordingly
    signal, sampling_rate = open_audio(fp)

## Version History

**0.1.2 (20.08.2019)**

Add instructions to install ffmpeg if load mp3 failed with ffmpeg backend not available. 

**0.1.1 (14.08.2019)**

Initial release.


