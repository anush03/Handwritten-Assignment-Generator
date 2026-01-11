import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, "static", "output")

PAGE_WIDTH, PAGE_HEIGHT = 2480, 3508
FONT_SIZE = 48
LINE_SPACING = 60
MARGIN_X, MARGIN_Y = 150, 200
TEXT_COLOR = (20, 20, 20)

# ✅ Font Map (KEY = UI value, VALUE = file path)
FONTS = {
    "patrick": os.path.join(BASE_DIR, "static", "fonts", "PatrickHand.ttf"),
    "caveat": os.path.join(BASE_DIR, "static", "fonts", "Caveat.ttf"),
    "dancing": os.path.join(BASE_DIR, "static", "fonts", "DancingScript.ttf"),
}

DEFAULT_FONT = "patrick"
