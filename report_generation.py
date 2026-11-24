
import pandas as pd
from io import StringIO, BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table
)
from reportlab.lib.styles import getSampleStyleSheet


def create_dataframe(detections):

    records = []

    for i, tree in enumerate(detections, start=1):

        x1, y1, x2, y2 = tree["bbox"]

        records.append({
            "Tree ID": i,
            "X1": x1,
            "Y1": y1,
            "X2": x2,
            "Y2": y2,
            "Confidence": tree["confidence"]
        })

    return pd.DataFrame(records)


def generate_csv(detections):

    df = create_dataframe(detections)

    output = StringIO()

    df.to_csv(output, index=False)

    return output.getvalue()


def generate_pdf(detections):

    df = create_dataframe(detections)

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "TREE ENUMERATION REPORT",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Total Trees Detected: {len(detections)}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 15))

    table_data = [list(df.columns)] + df.values.tolist()

    elements.append(Table(table_data))

    document.build(elements)

    buffer.seek(0)

    return buffer.getvalue()
