"""
HA Print Center printer interface.

Handles:
- PostScript encoding
- Base64 conversion
- IPP Printing service calls
"""

import base64


PRINTER_DEVICE_ID = "ba5034b6964b202c4177a5bc0ed5485c"


def encode_document(postscript):
    """
    Convert PostScript text into Base64.
    """

    raw = postscript.encode("utf-8")

    return base64.b64encode(raw).decode("ascii")


def print_postscript(postscript):
    """
    Send PostScript document to IPP printer.
    """

    encoded = encode_document(postscript)

    service.call(
        "ipp_printing",
        "print",
        {
            "mimetype": "application/postscript",
            "data": encoded,
        },
        target={
            "device_id": PRINTER_DEVICE_ID
        },
    )
