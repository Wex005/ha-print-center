"""
HA Print Center Document Engine

Defines the basic document structure.
"""


class Document:
    """
    Represents a printable document.
    """

    def __init__(self):
        self.elements = []

    def add_title(self, text):
        """
        Add a document title.
        """
        self.elements.append(
            {
                "type": "title",
                "content": text,
            }
        )

    def add_subtitle(self, text):
        """
        Add a document subtitle.
        """
        self.elements.append(
            {
                "type": "subtitle",
                "content": text,
            }
        )

    def add_text(self, text):
        """
        Add normal document text.
        """
        self.elements.append(
            {
                "type": "text",
                "content": text,
            }
        )

    def add_footer(self, text):
        """
        Add a document footer.
        """
        self.elements.append(
            {
                "type": "footer",
                "content": text,
            }
        )

    def get_elements(self):
        """
        Return all document elements.
        """
        return self.elements
