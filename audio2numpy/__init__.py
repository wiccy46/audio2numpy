import logging
from warnings import warn
from .loader import audio_from_file
import numpy as np
# from exceptions import DecodeError, NoBackendError

_LOGGER = logging.getLogger(__name__)
_LOGGER.addHandler(logging.NullHandler())

def open_audio(path):
    if ".mp3" in path:
        _LOGGER.info(" Mp3 file")
        sig, sr = audio_from_file(path, dtype=np.float32)
        return sig, sr
    elif ".wav" in path:
        _LOGGER.info(" Wav file")
        sig, sr = 0, 0
        return sig, sr
    else:
        warn(" mp3 and wav only, return 0")
        return 0, 0
        