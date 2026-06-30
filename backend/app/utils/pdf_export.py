from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
)


def export_pdf(markdown: str) -> BytesIO:
    """
    Convert Markdown to PDF.

    Supported Markdown:

    # Heading 1
    ## Heading 2
    ### Heading 3
    - Bullet List
    Paragraph
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    bullet_items = []

    def flush_bullets():
        nonlocal bullet_items

        if bullet_items:
            story.append(
                ListFlowable(
                    [
                        ListItem(
                            Paragraph(item, styles["BodyText"])
                        )
                        for item in bullet_items
                    ]
                )
            )
            bullet_items = []

    for line in markdown.splitlines():

        line = line.strip()

        if not line:
            flush_bullets()
            story.append(
                Paragraph("<br/>", styles["BodyText"])
            )
            continue

        if line.startswith("# "):
            flush_bullets()
            story.append(
                Paragraph(line[2:], styles["Heading1"])
            )

        elif line.startswith("## "):
            flush_bullets()
            story.append(
                Paragraph(line[3:], styles["Heading2"])
            )

        elif line.startswith("### "):
            flush_bullets()
            story.append(
                Paragraph(line[4:], styles["Heading3"])
            )

        elif line.startswith("- "):
            bullet_items.append(line[2:])

        else:
            flush_bullets()
            story.append(
                Paragraph(line, styles["BodyText"])
            )

    flush_bullets()

    document.build(story)

    buffer.seek(0)

    return buffer