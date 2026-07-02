import { FileText } from "lucide-react";

export function EmptyReport() {
  return (
    <div className="flex h-full flex-col items-center justify-center text-center">
      <div className="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-primary/10">
        <FileText className="h-10 w-10 text-primary" />
      </div>

      <h2 className="text-xl font-semibold">
        No Report Generated
      </h2>

      <p className="mt-2 max-w-sm text-sm text-muted-foreground">
        Enter a prompt and click
        <strong> Generate Report </strong>
        to see the AI generated report here.
      </p>
    </div>
  );
}