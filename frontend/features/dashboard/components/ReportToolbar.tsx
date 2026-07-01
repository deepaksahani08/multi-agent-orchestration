import {
  Copy,
  Download,
  FileText,
} from "lucide-react";

import { Button } from "@/components/ui/button";

export function ReportToolbar() {
  return (
    <div className="flex items-center justify-between border-b px-6 py-4">
      <div>
        <h2 className="text-lg font-semibold">
          Report Preview
        </h2>

        <p className="text-sm text-muted-foreground">
          Markdown Preview
        </p>
      </div>

      <div className="flex gap-2">
        <Button variant="outline" size="icon">
          <Copy className="h-4 w-4" />
        </Button>

        <Button variant="outline">
          <Download className="mr-2 h-4 w-4" />
          PDF
        </Button>

        <Button variant="outline">
          <FileText className="mr-2 h-4 w-4" />
          DOCX
        </Button>
      </div>
    </div>
  );
}