import numpy as np 
import logging
from .mp3dec import ffmpeg_available, FFmpegAudioFile
from .wavdec import RawAudioFile
from .exceptions import DecodeError, NoBackendError, AudioFormatError

_LOGGER = logging.getLogger(__name__)
_LOGGER.addHandler(logging.NullHandler())


def _buf_to_float(x, n_bytes=2, dtype=np.float32):
    """Convert an integer buffer to floating point values.
    This is primarily useful when loading integer-valued wav data
    into numpy arrays.

    Parameters
    ----------
    x : np.ndarray [dtype=int]
        The integer-valued data buffer
    n_bytes : int [1, 2, 4]
        The number of bytes per sample in `x`
    dtype : numeric type
        The target output type (default: 32-bit float)
    
    Returns
    -------
    x_float : np.ndarray [dtype=float]
        The input data buffer cast to floating point
    """
    # Invert the scale of the data
    scale = 1. / float(1 << ((8 * n_bytes) - 1))
    # Construct the format string
    fmt = '<i{:d}'.format(n_bytes)
    # Rescale and format the data buffer
    return scale * np.frombuffer(x, fmt).astype(dtype)


def _audio_read(path):
    """Try to read audio file with back end one by one."""
    _LOGGER.debug("Audio read call.")
    if path.endswith(".wav") or path.endswith(".aif"):
        try:
            return RawAudioFile(path)
        except DecodeError:
            pass
    elif path.endswith(".mp3"):
        try:
            return FFmpegAudioFile(path)
        except DecodeError:
            pass
    else:
        raise AudioFormatError("Only support mp3, wav, aiff formats.")
    msg = """It is likely that ffmpeg is not yet installed. Please refer github repo for instruction. 
    MacOS: brew install ffmpeg.
    Linux: sudo apt-get install ffmpeg
    Windows: Download distribution from ffmpeg website, unzip, add the path of bin (e.g. `C:\ffmpeg\bin`) to system PATH."""
    raise NoBackendError(msg)


def audio_from_file(path, offset=0, duration=None, dtype=np.float32):
    '''Load an audio buffer using audioread.
    This loads one block at a time, and then concatenates the results.

    Parameters
    ----------
    path : string
        File path
    offset : int (optional)
        sample offset of the loading start
    duration : None or float (optional)
        duration in seconds
    dtype : numpy dtype (optional)
        data type. By default float32
    '''
    y = []  # audio array
    with _audio_read(path) as input_file:
        sr_native = input_file.samplerate
        n_channels = input_file.channels
        s_start = int(np.round(sr_native * offset)) * n_channels

        if duration is None:
            s_end = np.inf
        else:
            s_end = s_start + (int(np.round(sr_native * duration)) * n_channels)
        n = 0
        for frame in input_file:
            frame = _buf_to_float(frame, dtype=dtype)
            n_prev = n
            n = n + len(frame)
            if n < s_start:
                # offset is after the current frame
                # keep reading
                continue
            if s_end < n_prev:
                # we're off the end.  stop reading
                break
            if s_end < n:
                # the end is in this frame.  crop.
                frame = frame[:s_end - n_prev]
            if n_prev <= s_start <= n:
                # beginning is in this frame
                frame = frame[(s_start - n_prev):]
            # tack on the current frame
            y.append(frame)

    if y:
        y = np.concatenate(y)
        if n_channels > 1:
            y = y.reshape((-1, n_channels))
    else:
        y = np.empty(0, dtype=dtype)
        sr_native = 0
    return y, sr_native