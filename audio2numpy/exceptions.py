class DecodeError(Exception):
    """The base exception class for all decoding errors raised by this
    package."""


class NoBackendError(DecodeError):
    """The file could not be decoded by any backend. Either no backends
    are available or each available backend failed to decode the file.
    """

class DataError(DecodeError):
    """Unknown data"""

class AudioFormatError(DecodeError):
    """Audio file is not a supported audio format"""


class FFmpegError(DecodeError):
    pass


class NotInstalledError(FFmpegError):
    """Could not find the ffmpeg binary."""


class ReadTimeoutError(FFmpegError):
    """Reading from the ffmpeg command-line tool timed out."""


class CommunicationError(FFmpegError):
    """Raised when the output of FFmpeg is not parseable."""
