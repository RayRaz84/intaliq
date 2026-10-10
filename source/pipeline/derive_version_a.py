"""Owner-authorized, localized Version A composites; no other art is redrawn."""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'art-production/v43-support'
OUT.mkdir(parents=True, exist_ok=True)
book_path = ROOT / 'source/cast-and-art/references/rich-cartoon/version-a-generated-book.png'
book = Image.open(book_path).convert('RGBA')
book = book.crop(book.getbbox())
records = {}
for frame, position, size, rect in [
    (2, (815, 931), (170, 108), (815, 931, 220, 110)),
    (7, (1074, 757), (230, 86), (1074, 757, 230, 86)),
]:
    source = ROOT / f'assets/art/unit2-rich/u2-s1-{frame}.png'
    original = Image.open(source).convert('RGBA')
    revised = original.copy()
    revised.alpha_composite(book.resize(size, Image.Resampling.LANCZOS), position)
    if frame == 7:
        # Re-layer the original cat paws/body over the inserted book, without moving them.
        mask = Image.new('L', original.size)
        ImageDraw.Draw(mask).polygon([
            (1100, 757), (1245, 757), (1261, 751), (1283, 747),
            (1290, 771), (1279, 788), (1242, 793), (1238, 798),
            (1225, 800), (1194, 801), (1180, 799), (1166, 802),
            (1145, 800), (1128, 799), (1106, 798), (1099, 792),
        ], fill=255)
        revised.paste(original, (0, 0), mask)
    bbox = ImageChops.difference(original, revised).convert('RGB').getbbox()
    x, y, w, h = rect
    assert bbox and bbox[0] >= x and bbox[1] >= y and bbox[2] <= x+w and bbox[3] <= y+h
    target = OUT / f'u2-va-{frame}-derived.png'
    revised.save(target)
    records[f'u2-va-{frame}'] = {
        'source_slot': f'u2-s1-{frame}', 'changed_rect': rect,
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'generated_book_sha256': hashlib.sha256(book_path.read_bytes()).hexdigest(),
        'authorization': 'Owner explicit Version A-only targeted compositing approval; SC-115',
        'method': 'Localized alpha composite of generated book; original cat pixels re-layered in frame 7',
        'changed_bbox': bbox,
    }
(OUT / 'derivations.json').write_text(json.dumps(records, indent=2) + '\n')
