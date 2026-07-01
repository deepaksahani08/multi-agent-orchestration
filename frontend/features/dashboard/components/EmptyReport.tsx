import { Sparkles } from "lucide-react";

export function EmptyReport() {
  return (
    <div className="flex h-full flex-col items-center justify-center px-8 text-center">
      <div className="mb-6 flex size-20 items-center justify-center rounded-full bg-primary/10">
        <Sparkles className="size-10 text-primary" />
      </div>

      <h2 className="text-xl font-semibold">
        No report generated
      </h2>

      <p className="mt-3 max-w-sm text-sm text-muted-foreground">
        Generate a report from the prompt panel.
        Your AI-generated report will appear here.
      </p>
    </div>
  );
}