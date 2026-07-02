import { api } from "@/lib/api";
import { slugify } from "@/lib/slugify";

function downloadBlob(blob: Blob, filename: string) {
  const url = window.URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;
  link.download = filename;

  document.body.appendChild(link);

  link.click();

  link.remove();

  window.URL.revokeObjectURL(url);
}

export function downloadMarkdown(
  markdown: string,
  prompt: string
) {
  const blob = new Blob([markdown], {
    type: "text/markdown;charset=utf-8",
  });

  downloadBlob(blob, `${slugify(prompt)}.md`);
}

export async function downloadPDF(
  markdown: string,
  prompt: string
) {
  const response = await api.post(
    "/download/pdf",
    { markdown },
    {
      responseType: "blob",
    }
  );

  downloadBlob(
    response.data,
    `${slugify(prompt)}.pdf`
  );
}

export async function downloadDOCX(
  markdown: string,
  prompt: string
) {
  const response = await api.post(
    "/download/docx",
    { markdown },
    {
      responseType: "blob",
    }
  );

  downloadBlob(
    response.data,
    `${slugify(prompt)}.docx`
  );
}