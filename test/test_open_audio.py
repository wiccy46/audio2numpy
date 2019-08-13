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
