import wave
import aifc
import sys
import audioop
import struct
from .exceptions import DecodeError


# Produce two-byte (16-bit) output samples.
TARGET_WIDTH = 2
# Python 3.4 added support for 24-bit (3-byte) samples.
if sys.version_info > (3, 4, 0):
    SUPPORTED_WIDTHS = (1, 2, 3, 4)
else:
    SUPPORTED_WIDTHS = (1, 2, 4)


class UnsupportedError(DecodeError):
    """File is not an AIFF, WAV, or Au file."""


class BitWidthError(DecodeError):
    """The file uses an unsupported bit width."""


class RawAudioFile(object):
    """An AIFF, WAV, or Au file that can be read by the Python standard
    library modules ``wave``, ``aifc``, and ``sunau``."""
    def __init__(self, filename):
        self._fh = open(filename, 'rb')  
        try:  # aifc format
            self._file = aifc.open(self._fh)
        except aifc.Error:
            # Return to the beginning of the file to try the next reader.
            self._fh.seek(0)
        else:
            self._needs_byteswap = True
            self._check()
            return

        try:  # .wav format
            self._file = wave.open(self._fh)
        except wave.Error:
            self._fh.seek(0)
            pass
        else:
            self._needs_byteswap = False
            self._check()
            return

        # None of the three libraries could open the file.
        self._fh.close()
        raise UnsupportedError()

    def _check(self):
        """Check that the files' parameters allow us to decode it and
        raise an error otherwise.
        """
        if self._file.getsampwidth() not in SUPPORTED_WIDTHS:
            self.close()
            raise BitWidthError()

    def close(self):
        """Close the underlying file."""
        self._file.close()
        self._fh.close()

    @property
    def channels(self):
        """Number of audio channels."""
        return self._file.getnchannels()

    @property
    def samplerate(self):
        """Sample rate in Hz."""
        return self._file.getframerate()

    @property
    def duration(self):
        """Length of the audio in seconds (a float)."""
        return float(self._file.getnframes()) / self.samplerate

    def read_data(self, block_samples=1024):
        """Generates blocks of PCM data found in the file."""
        old_width = self._file.getsampwidth()

        while True:
            data = self._file.readframes(block_samples)
            if not data:
                break

            # Make sure we have the desired bitdepth and endianness.
            data = audioop.lin2lin(data, old_width, TARGET_WIDTH)
            if self._needs_byteswap and self._file.getcomptype() != 'sowt':
                # Big-endian data. Swap endianness.
                data = self.byteswap(data)
            yield data

    def byteswap(self, s):
        """Swaps the endianness of the bytesting s, which must be an array
        of shorts (16-bit signed integers). This is probably less efficient
        than it should be.
        """
        assert len(s) % 2 == 0
        parts = []
        for i in range(0, len(s), 2):
            chunk = s[i: i + 2]
            newchunk = struct.pack('<h', *struct.unpack('>h', chunk))
            parts.append(newchunk)
        return b''.join(parts)

    # Context manager.
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    # Iteration.
    def __iter__(self):
        return self.read_data()
