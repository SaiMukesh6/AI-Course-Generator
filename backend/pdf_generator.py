from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import darkblue
from reportlab.lib.units import inch


def create_pdf(course, filename="course.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER
    title_style.textColor = darkblue

    heading_style = styles["Heading2"]

    normal_style = styles["BodyText"]

    story = []

    story.append(Paragraph("AI COURSE GENERATOR", title_style))
    story.append(Spacer(1, 0.3 * inch))

    for line in course.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):

            story.append(
                Paragraph(
                    line.replace("#", "").strip(),
                    heading_style
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    normal_style
                )
            )

        story.append(Spacer(1, 0.1 * inch))

    story.append(Spacer(1, 0.3 * inch))

    story.append(
        Paragraph(
            "<b>Generated using AI Course Generator</b>",
            normal_style
        )
    )

    doc.build(story)

    return filename