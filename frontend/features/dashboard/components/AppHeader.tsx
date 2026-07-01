import { Bot } from "lucide-react";
import { Button } from "@/components/ui/button";

export function AppHeader() {
  return (
    <header className="sticky top-0 z-50 flex h-16 items-center justify-between border-b bg-background/95 px-6 backdrop-blur">
      <div className="flex items-center gap-3">
        <div className="flex size-10 items-center justify-center rounded-xl bg-primary text-primary-foreground">
          <Bot className="size-5" />
        </div>

        <div>
          <h1 className="text-lg font-semibold tracking-tight">
            Multi-Agent Platform
          </h1>

          <p className="text-xs text-muted-foreground">
            AI Workflow Orchestration
          </p>
        </div>
      </div>

      <Button variant="outline">
        Documentation
      </Button>
    </header>
  );
}