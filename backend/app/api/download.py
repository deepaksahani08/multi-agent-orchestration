from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.export import ExportRequest
from app.utils.docx_export import export_docx
from app.utils.pdf_export import export_pdf

router = APIRouter(prefix="/download", tags=["Download"])


@router.post("/pdf")
async def download_pdf(request: ExportRequest):

    pdf = export_pdf(request.markdown)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": 'attachment; filename="report.pdf"',
        },
    )


@router.post("/docx")
async def download_docx(request: ExportRequest):

    docx = export_docx(request.markdown)

    return StreamingResponse(
        docx,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": 'attachment; filename="report.docx"',
        },
    )