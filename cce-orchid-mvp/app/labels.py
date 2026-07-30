from io import BytesIO
import qrcode
from reportlab.lib.pagesizes import landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from .models import Thing


def build_orchid_label_pdf(thing: Thing, public_base_url: str) -> bytes:
    width, height = landscape((1 * inch, 4 * inch))
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=(width, height))
    pdf.setTitle(f"Label {thing.accession_number}")

    url = f"{public_base_url.rstrip('/')}/p/{thing.label_id}"
    qr = qrcode.QRCode(version=None, box_size=8, border=1)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_buffer = BytesIO()
    qr_img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)

    margin = 0.12 * inch
    qr_size = 0.78 * inch
    pdf.drawImage(ImageReader(qr_buffer), width - margin - qr_size, (height - qr_size) / 2, qr_size, qr_size)

    text_width = width - qr_size - (3 * margin)
    text = pdf.beginText(margin, height - 0.22 * inch)
    text.setFont("Helvetica-Bold", 10)
    words = thing.display_name.split()
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if pdf.stringWidth(candidate, "Helvetica-Bold", 10) <= text_width:
            line = candidate
        else:
            text.textLine(line)
            line = word
    if line:
        text.textLine(line)

    text.setFont("Helvetica", 8)
    text.moveCursor(0, 4)
    text.textLine(thing.accession_number)
    if thing.location:
        location = thing.location.path
        while pdf.stringWidth(location, "Helvetica", 7) > text_width and len(location) > 12:
            location = location[:-4] + "..."
        text.setFont("Helvetica", 7)
        text.textLine(location)
    pdf.drawText(text)

    pdf.setFont("Helvetica", 5.5)
    pdf.drawString(margin, 0.08 * inch, "orchid-enthusiasts.com")
    pdf.showPage()
    pdf.save()
    return buffer.getvalue()
