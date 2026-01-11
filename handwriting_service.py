from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import textwrap
import os
from config import *
from utils import ensure_output_dir

def generate_handwritten_pages(text: str, font_key: str):
    ensure_output_dir()

    # Fallback protection
    font_path = FONTS.get(font_key, FONTS[DEFAULT_FONT])

    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font not found: {font_path}")

    font = ImageFont.truetype(font_path, FONT_SIZE)

    wrapped_lines = textwrap.wrap(text, width=80)

    pages, current_page = [], []
    current_height = MARGIN_Y

    for line in wrapped_lines:
        if current_height + LINE_SPACING > PAGE_HEIGHT - MARGIN_Y:
            pages.append(current_page)
            current_page = []
            current_height = MARGIN_Y

        current_page.append(line)
        current_height += LINE_SPACING

    if current_page:
        pages.append(current_page)

    image_paths = []

    for idx, page in enumerate(pages, start=1):
        img = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "white")
        draw = ImageDraw.Draw(img)

        y = MARGIN_Y
        for line in page:
            draw.text((MARGIN_X, y), line, fill=TEXT_COLOR, font=font)
            y += LINE_SPACING

        path = os.path.join(OUTPUT_DIR, f"page_{idx}.png")
        img.save(path)
        image_paths.append(path)

    return image_paths


def generate_pdf(image_paths):
    pdf_path = os.path.join(OUTPUT_DIR, "assignment.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)

    for img in image_paths:
        c.drawImage(img, 0, 0, width=A4[0], height=A4[1])
        c.showPage()

    c.save()
    return pdf_path
