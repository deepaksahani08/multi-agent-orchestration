"use client";

import {
  Copy,
  Download,
  RotateCcw,
} from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  downloadDOCX,
  downloadMarkdown,
  downloadPDF,
} from "@/services/download-service";
import { useWorkflowStore } from "@/store/workflow-store";

export function ReportToolbar() {
  const {
    report,
    prompt,
    reset,
  } = useWorkflowStore();

  async function handleCopy() {
    if (!report) {
      toast.error("No report available.");
      return;
    }

    try {
      await navigator.clipboard.writeText(report);
      toast.success("Report copied to clipboard.");
    } catch {
      toast.error("Failed to copy report.");
    }
  }

  function handleMarkdown() {
    if (!report) {
      toast.error("No report available.");
      return;
    }

    downloadMarkdown(report, prompt);

    toast.success("Markdown downloaded.");
  }

  async function handlePDF() {
    if (!report) {
      toast.error("No report available.");
      return;
    }

    try {
      await downloadPDF(report, prompt);

      toast.success("PDF downloaded.");
    } catch {
      toast.error("Failed to download PDF.");
    }
  }

  async function handleDOCX() {
    if (!report) {
      toast.error("No report available.");
      return;
    }

    try {
      await downloadDOCX(report, prompt);

      toast.success("DOCX downloaded.");
    } catch {
      toast.error("Failed to download DOCX.");
    }
  }

  function handleReset() {
    reset();
    toast.success("Workspace cleared.");
  }

  return (
    <div className="flex items-center justify-between border-b px-6 py-5">
      {/* Left */}
      {/* <div className="flex items-center gap-3">
        <h2 className="text-xl font-bold">
          Report Preview
        </h2>

        <span className="rounded-full bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
          AI Generated Markdown
        </span>
      </div> */}

      {/* Right */}
      <div className="flex items-center gap-2">
        <Button
          variant="outline"
          size="icon"
          onClick={handleCopy}
          disabled={!report}
        >
          <Copy className="h-4 w-4" />
        </Button>

        <Button
          variant="outline"
          onClick={handleMarkdown}
          disabled={!report}
        >
          <Download className="mr-2 h-4 w-4" />
          Markdown
        </Button>

        <Button
          variant="outline"
          onClick={handlePDF}
          disabled={!report}
        >
          PDF
        </Button>

        <Button
          variant="outline"
          onClick={handleDOCX}
          disabled={!report}
        >
          DOCX
        </Button>

        <Button
          variant="outline"
          onClick={handleReset}
        >
          <RotateCcw className="mr-2 h-4 w-4" />
          New
        </Button>
      </div>
    </div>
  );
}