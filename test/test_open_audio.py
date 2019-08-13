from audio2numpy import open_audio
from unittest import TestCase
import logging
logging.basicConfig(level=logging.INFO)


class TestLoad(TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_mp3(self):
        fp = "./examples/word.mp3"
        s, sr = open_audio(fp)
        self.assertEqual(24000, sr)
        self.assertEqual(16128, s.shape[0])

    def test_wav(self):
        fp = "./examples/word.wav"
        s, sr = open_audio(fp)
        self.assertEqual(24000, sr)
        self.assertEqual(16128, s.shape[0])

    def test_aiff(self):
        fp = "./examples/chord.aif"
        s, sr = open_audio(fp)
        self.assertEqual(128000, s.shape[0])
        self.assertEqual(32000, sr)

