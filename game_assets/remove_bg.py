import sys
from pathlib import Path
from rembg import remove


def convert_to_png_no_bg(src_path: Path, dst_path: Path | None = None) -> None:
    """
    Convert a BMP/JPG (or any format Pillow can open) to PNG with the background removed.
    """
    if not src_path.is_file():
        raise FileNotFoundError(f"Source file not found: {src_path}")

    # Destination defaults to the same stem with a .png suffix
    dst_path = dst_path or src_path.with_suffix(".png")

    # 1️⃣  Read the *encoded* image bytes
    with open(src_path, "rb") as f:
        input_bytes = f.read()

    # 2️⃣  Run the background‑matting model
    output_bytes = remove(input_bytes)

    # 3️⃣  Write the PNG
    with open(dst_path, "wb") as f:
        f.write(output_bytes)

    print(f"✅  {src_path} → {dst_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_bg.py <image_path> [output_path]")
        sys.exit(1)

    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    convert_to_png_no_bg(src, out)
