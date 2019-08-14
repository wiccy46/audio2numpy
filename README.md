# audio2numpy
[![Build Status](https://travis-ci.com/wiccy46/audio2numpy.svg?branch=master)](https://travis-ci.com/wiccy46/audio2numpy)

## Description

audio2numpy load an audio file and directly ouputs the audio data as a numpy array and its sampling rate. Supports .wav, .aiff via python's standard library, and .mp3 via ffmpeg.

## Installation

Using pip:

    pip install audio2numpy

## Usage

    from audio2numpy import open_audio
    fp = "./examples/word.mp3"  # change to the correct path to your file accordingly
    signal, sampling_rate = open_audio(fp)