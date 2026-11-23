"""TASK 3 tests: python -m unittest tests.test_task3_detect -v"""
import unittest

from PIL import Image

from stegolab.detect import analyse, find_appended_data, lsb_ratios, make_lsb_plane, read_metadata
from stegolab.embed import hide_message
from tests.helpers import gradient_png, png_with_text, tmp_path


class Task3Detect(unittest.TestCase):
    def test_no_appended_data(self):
        self.assertEqual(find_appended_data(gradient_png()), b"")

    def test_appended_data_found(self):
        path = gradient_png()
        with open(path, "ab") as fh:
            fh.write(b"secret")
        self.assertEqual(find_appended_data(path), b"secret")

    def test_metadata_found(self):
        self.assertEqual(read_metadata(png_with_text("Comment", "hi"))["Comment"], "hi")

    def test_no_metadata(self):
        self.assertEqual(read_metadata(gradient_png()), {})

    def test_lsb_ratios_range(self):
        ratios = lsb_ratios(gradient_png())
        self.assertTrue(0 <= ratios["start"] <= 1 and 0 <= ratios["whole"] <= 1)

    def test_lsb_plane_same_size(self):
        cover, plane = gradient_png(), tmp_path("plane.png")
        make_lsb_plane(cover, plane)
        self.assertEqual(Image.open(plane).size, Image.open(cover).size)

    def test_analyse_confirms_hidden_message(self):
        out = tmp_path("stego.png")
        hide_message(gradient_png(), "BCU{x}", out)
        self.assertTrue(any("confirmed" in f for f in analyse(out)["findings"]))

    def test_analyse_clean_image(self):
        self.assertEqual(analyse(gradient_png())["findings"], [])


if __name__ == "__main__":
    unittest.main()
