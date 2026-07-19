"""
HA Print Center test page.
"""


@service
def print_test_page():

    from .document import Document
    from .printer import print_postscript

    doc = Document()

    doc.text(
        72,
        720,
        "HA Print Center"
    )

    doc.text(
        72,
        690,
        "IPP Printing Test Successful"
    )

    doc.text(
        72,
        660,
        "HP LaserJet M402n"
    )

    print_postscript(
        doc.build()
    )
