"use client";

import { Card } from "@/components/ui/card";

import { useWorkflowStore } from "@/store/workflow-store";

import { EmptyReport } from "./EmptyReport";
import { MarkdownPreview } from "./MarkdownPreview";
import { ReportToolbar } from "./ReportToolbar";

export function ReportPanel() {
  const { report } = useWorkflowStore();

  return (
    <Card className="glass-card flex h-full flex-col overflow-hidden rounded-3xl">
      <ReportToolbar />

      <div className="min-h-0 flex-1 overflow-y-auto p-6">
        {report ? (
          <MarkdownPreview content={report} />
        ) : (
          <EmptyReport />
        )}
      </div>
    </Card>
  );
}