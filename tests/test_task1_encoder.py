"""TASK 1 tests: python -m unittest tests.test_task1_encoder -v"""
import unittest

from stegolab.encoder import MAGIC, bits_to_bytes, build_payload, bytes_to_bits, parse_header


class Task1Encoder(unittest.TestCase):
    def test_single_byte_to_bits(self):
        self.assertEqual(bytes_to_bits(b"A"), [0, 1, 0, 0, 0, 0, 0, 1])

    def test_bits_round_trip(self):
        data = b"BCU{test}\x00\xff"
        self.assertEqual(bits_to_bytes(bytes_to_bits(data)), data)

    def test_leftover_bits_ignored(self):
        self.assertEqual(bits_to_bytes([0, 1, 0, 0, 0, 0, 0, 1, 1, 1]), b"A")

    def test_payload_starts_with_header(self):
        bits = build_payload("hi")
        self.assertEqual(bits_to_bytes(bits[:32]), MAGIC)
        self.assertEqual(len(bits), (8 + 2) * 8)

    def test_header_parsed(self):
        self.assertEqual(parse_header(build_payload("hello")), 5)

    def test_unicode_length_is_in_bytes(self):
        self.assertEqual(parse_header(build_payload("£")), 2)

    def test_no_magic_returns_none(self):
        self.assertIsNone(parse_header([0] * 64))

    def test_too_short_returns_none(self):
        self.assertIsNone(parse_header([1, 0, 1]))


if __name__ == "__main__":
    unittest.main()
