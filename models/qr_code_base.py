# -*- coding: utf-8 -*-
import qrcode
import base64
import io
from io import BytesIO

def generate_qr_code(qr_string):
    qr = qrcode.QRCode(version=4, box_size=4, border=1)
    qr.add_data(qr_string)
    qr.make(fit=True)
    img = qr.make_image()
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue())
    return img_str
