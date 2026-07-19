"""
Basic PostScript document builder.
"""


class Document:

    def __init__(self):
        self.lines = [
            "%!PS-Adobe-3.0",
            "%%Pages: 1",
            "/Helvetica findfont 12 scalefont setfont",
        ]


    def text(self, x, y, message):
        message = (
            message
            .replace("\\", "\\\\")
            .replace("(", "\\(")
            .replace(")", "\\)")
        )

        self.lines.append(
            f"{x} {y} moveto ({message}) show"
        )


    def build(self):

        self.lines.append("showpage")
        self.lines.append("%%EOF")

        return "\n".join(self.lines)
