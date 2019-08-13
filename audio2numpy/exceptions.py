class DecodeError(Exception):
    """The base exception class for all decoding errors raised by this
    package."""


class NoBackendError(DecodeError):
    """The file could not be decoded by any backend. Either no backends
    are available or each available backend failed to decode the file.
    """