"""TASK 2 - Embed: hide bits in the least significant bit (LSB) of each colour value.

THE IDEA
    Every pixel has three colour values (Red, Green, Blue), each 0-255. Changing the LAST bit of a
    value changes it by at most 1, e.g. 200 -> 201. Your eye cannot see that difference, but a
    program can read it back. Three hidden bits fit in every pixel.

    We walk the pixels left-to-right, top-to-bottom, and the channels in the order R, G, B.

HOW YOU KNOW YOU ARE DONE
    python -m unittest tests.test_task2_embed -v
"""
from __future__ import annotations

from typing import List

from PIL import Image

from stegolab.encoder import HEADER_BYTES, bits_to_bytes, build_payload, parse_header


def capacity_bits(img: Image.Image) -> int:
    """How many bits fit in this image (3 per pixel)."""
    width, height = img.size
    return width * height * 3


def set_lsb(value: int, bit: int) -> int:
    """Return ``value`` with its least significant bit replaced by ``bit``."""
    # TODO 2.1  Clear the last bit with  value & ~1  then set it with  | bit.
    raise NotImplementedError("TODO (Task 2.1)")


def hide_message(cover_path: str, message: str, output_path: str) -> int:
    """Hide ``message`` in the image at ``cover_path`` and save a PNG to ``output_path``.

    Returns the number of bits written. Raises ValueError if the message does not fit.
    """
    img = Image.open(cover_path).convert("RGB")
    # TODO 2.2  bits = build_payload(message)
    #           If len(bits) > capacity_bits(img): raise ValueError with a helpful message.
    #           channels = list(img.tobytes())   -> a flat list R,G,B,R,G,B,...
    #           For each (i, bit): channels[i] = set_lsb(channels[i], bit)
    #           stego = Image.frombytes("RGB", img.size, bytes(channels))
    #           Save it as PNG (why not JPEG? see the README) and return len(bits).
    raise NotImplementedError("TODO (Task 2.2)")


def read_lsbs(img: Image.Image, count: int) -> List[int]:
    """Return the first ``count`` least significant bits in R,G,B pixel order."""
    # TODO 2.3  channels = img.convert("RGB").tobytes()
    #           Return the last bit (value & 1) of the first `count` values.
    raise NotImplementedError("TODO (Task 2.3)")


def reveal_message(stego_path: str) -> str | None:
    """Return the hidden message, or None if the image carries no StegoLab header."""
    img = Image.open(stego_path)
    # TODO 2.4  length = parse_header(read_lsbs(img, HEADER_BYTES * 8))
    #           If length is None, or the message would not fit in the image, return None.
    #           Read (HEADER_BYTES + length) * 8 bits, drop the header bits,
    #           turn the rest into bytes and decode as UTF-8 (errors="replace").
    raise NotImplementedError("TODO (Task 2.4)")


