"""
HA Print Center Renderer

Converts documents into output formats.
"""


class DebugRenderer:
    """
    Simple renderer for testing document output.
    """

    def render(self, document):
        """
        Convert a document into readable text.
        """

        output = []

        for element in document.get_elements():

            element_type = element["type"]
            content = element["content"]

            if element_type == "title":
                output.append("=" * 40)
                output.append(content.upper())
                output.append("=" * 40)

            elif element_type == "subtitle":
                output.append(content)

            elif element_type == "text":
                output.append(content)

            elif element_type == "footer":
                output.append("-" * 40)
                output.append(content)

        return "\n".join(output)
