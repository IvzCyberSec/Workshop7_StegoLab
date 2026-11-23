"""TASK 2 tests: python -m unittest tests.test_task2_embed -v"""
import unittest

from PIL import Image

from stegolab.embed import capacity_bits, hide_message, reveal_message, set_lsb
from tests.helpers import gradient_png, tmp_path


class Task2Embed(unittest.TestCase):
    def test_set_lsb(self):
        self.assertEqual(set_lsb(200, 1), 201)
        self.assertEqual(set_lsb(201, 0), 200)
        self.assertEqual(set_lsb(255, 1), 255)

    def test_capacity(self):
        self.assertEqual(capacity_bits(Image.new("RGB", (10, 4))), 120)

    def test_hide_and_reveal(self):
        out = tmp_path("stego.png")
        hide_message(gradient_png(), "BCU{hidden}", out)
        self.assertEqual(reveal_message(out), "BCU{hidden}")

    def test_pixels_change_by_at_most_one(self):
        cover, out = gradient_png(), tmp_path("stego.png")
        hide_message(cover, "a fairly long secret message " * 5, out)
        before = Image.open(cover).convert("RGB").tobytes()
        after = Image.open(out).convert("RGB").tobytes()
        self.assertTrue(all(abs(a - b) <= 1 for a, b in zip(before, after)))

    def test_message_too_big(self):
        with self.assertRaises(ValueError):
            hide_message(gradient_png(4, 4), "x" * 100, tmp_path("stego.png"))

    def test_clean_image_reveals_nothing(self):
        self.assertIsNone(reveal_message(gradient_png()))


if __name__ == "__main__":
    unittest.main()
