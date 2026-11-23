"""Prebuilt: prints the forensic report. It only formats results; it does no analysis itself."""
from __future__ import annotations

from typing import Dict


def preview(data: bytes, limit: int = 60) -> str:
    text = data[:limit].decode("utf-8", errors="replace")
    return text + ("..." if len(data) > limit else "")


def print_report(result: Dict) -> None:
    line = "=" * 60
    print(line)
    print(f"  StegoLab forensic report: {result['file']}")
    print(line)
    lsb = result["lsb"]
    print(f"  LSB share of 1s  start {lsb['start']:.3f} | whole {lsb['whole']:.3f}  (context only - check the LSB plane)")
    if result["appended"]:
        print(f"  Appended data    {len(result['appended'])} bytes: {preview(result['appended'])}")
    else:
        print("  Appended data    none")
    if result["metadata"]:
        for key, value in result["metadata"].items():
            print(f"  Metadata         {key} = {preview(value.encode())}")
    else:
        print("  Metadata         none")
    print("-" * 60)
    if result["findings"]:
        for finding in result["findings"]:
            print(f"  [!] {finding}")
    else:
        print("  No indicators found. (This does NOT prove the file is clean.)")
    print(line)
