import logging
from warnings import warn
from .loader import audio_from_file
import numpy as np
# from exceptions import DecodeError, NoBackendError

_LOGGER = logging.getLogger(__name__)
_LOGGER.addHandler(logging.NullHandler())

def open_audio(path):
    sig, sr = audio_from_file(path, dtype=np.float32)
    return sig, sr

        