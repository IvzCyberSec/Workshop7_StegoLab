"""TASK 1 - Encoder: turn a secret message into bits, and bits back into a message.

WHY THIS EXISTS
    Images store numbers, not text. Before we can hide a message inside pixels we need it as a
    stream of 1s and 0s. Before the message itself we put a small HEADER so the extractor knows
    (a) that a hidden message is really there and (b) how long it is:

        MAGIC (4 bytes: b"BCU7")  +  LENGTH (4 bytes, big-endian)  +  MESSAGE (UTF-8 bytes)

HOW YOU KNOW YOU ARE DONE
    python -m unittest tests.test_task1_encoder -v
"""
from __future__ import annotations

from typing import List

MAGIC = b"BCU7"          # marks "a StegoLab message starts here"
HEADER_BYTES = 8          # 4 bytes magic + 4 bytes length


def bytes_to_bits(data: bytes) -> List[int]:
    """Return every bit of ``data``, most significant bit first.

    Example: b"A" (65 = 0b01000001) -> [0, 1, 0, 0, 0, 0, 0, 1]
    """
    # TODO 1.1  Create an empty list.
    #           For each byte, loop over shift = 7, 6, ... 0 and append (byte >> shift) & 1.
    #           Hint: >> moves bits right; & 1 keeps only the last bit.
    raise NotImplementedError("TODO (Task 1.1)")


def bits_to_bytes(bits: List[int]) -> bytes:
    """Inverse of bytes_to_bits. Ignores any leftover bits that do not make a full byte."""
    # TODO 1.2  Walk through the bits 8 at a time (only full groups of 8).
    #           Start value = 0; for each bit: value = (value << 1) | bit.
    #           Append value to a bytearray and return bytes(...).
    raise NotImplementedError("TODO (Task 1.2)")


def build_payload(message: str) -> List[int]:
    """Return the full bit stream to hide: MAGIC + 4-byte length + UTF-8 message."""
    # TODO 1.3  body = message encoded as UTF-8.
    #           header = MAGIC + the body length as 4 big-endian bytes (int.to_bytes).
    #           Return bytes_to_bits(header + body).
    raise NotImplementedError("TODO (Task 1.3)")


def parse_header(bits: List[int]) -> int | None:
    """Read the first 64 bits. Return the message length in bytes, or None if MAGIC is absent."""
    # TODO 1.4  If there are fewer than HEADER_BYTES * 8 bits, return None.
    #           Convert the first 64 bits to bytes. If the first 4 bytes are not MAGIC, return None.
    #           Otherwise return the next 4 bytes as a big-endian integer (int.from_bytes).
    raise NotImplementedError("TODO (Task 1.4)")


