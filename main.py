"""StegoLab - hide, reveal and detect hidden data in images.

Usage:
    python main.py hide    <cover.png> "<message>" <output.png>
    python main.py reveal  <stego.png>
    python main.py analyse <suspect.png> [--plane lsb_plane.png]
"""
import argparse
import sys

from stegolab.detect import analyse, make_lsb_plane
from stegolab.embed import hide_message, reveal_message
from stegolab.report import print_report


def main() -> int:
    parser = argparse.ArgumentParser(description="StegoLab - BCUCompSoc Workshop 07")
    sub = parser.add_subparsers(dest="command", required=True)
    p_hide = sub.add_parser("hide", help="hide a message in an image")
    p_hide.add_argument("cover"); p_hide.add_argument("message"); p_hide.add_argument("output")
    p_rev = sub.add_parser("reveal", help="extract a hidden message")
    p_rev.add_argument("image")
    p_an = sub.add_parser("analyse", help="run forensic checks on an image")
    p_an.add_argument("image"); p_an.add_argument("--plane", help="save the LSB bit plane to this file")
    args = parser.parse_args()

    if args.command == "hide":
        bits = hide_message(args.cover, args.message, args.output)
        print(f"Hidden {bits} bits in {args.output}")
    elif args.command == "reveal":
        message = reveal_message(args.image)
        print(message if message is not None else "No StegoLab message found.")
    elif args.command == "analyse":
        print_report(analyse(args.image))
        if args.plane:
            make_lsb_plane(args.image, args.plane)
            print(f"LSB plane saved to {args.plane}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
