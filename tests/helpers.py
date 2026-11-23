import os
import tempfile

from PIL import Image, PngImagePlugin


def tmp_path(name: str) -> str:
    folder = tempfile.mkdtemp(prefix="stegolab_")
    return os.path.join(folder, name)


def gradient_png(width: int = 64, height: int = 48) -> str:
    """A small smooth test image (no hidden data)."""
    img = Image.new("RGB", (width, height))
    img.putdata([(x * 4 % 256, y * 5 % 256, 128) for y in range(height) for x in range(width)])
    path = tmp_path("cover.png")
    img.save(path)
    return path


def png_with_text(key: str, value: str) -> str:
    info = PngImagePlugin.PngInfo()
    info.add_text(key, value)
    path = tmp_path("meta.png")
    Image.new("RGB", (8, 8), (10, 20, 30)).save(path, pnginfo=info)
    return path
