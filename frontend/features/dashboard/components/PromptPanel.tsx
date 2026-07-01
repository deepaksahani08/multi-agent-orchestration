"use client";

import { Sparkles } from "lucide-react";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";

import { ExamplePrompts } from "./ExamplePrompts";

export function PromptPanel() {
  const [prompt, setPrompt] = useState("");

  return (
    <Card className="ai-composer rounded-[28px] border-0 p-8">
      <div className="space-y-8">
        {/* Header */}
        <div className="space-y-3">
          <span className="inline-flex items-center rounded-full bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
            <Sparkles className="mr-2 h-3.5 w-3.5" />
            AI Workspace
          </span>

          <h2 className="text-3xl font-bold tracking-tight">
            What would you like to research today?
          </h2>

          <p className="max-w-2xl text-muted-foreground">
            Transform your idea into a professional report using a team of
            specialized AI agents.
          </p>
        </div>

        {/* AI Composer */}
        <div className="overflow-hidden rounded-2xl border bg-background/70 backdrop-blur-sm transition-all focus-within:border-primary">
          <Textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Create a market research report for NVIDIA AI in 2026..."
            className="min-h-56 resize-none border-0 bg-transparent px-5 py-4 text-base shadow-none focus-visible:ring-0"
          />

          <div className="flex items-center justify-between border-t bg-white/40 px-5 py-4">
            <p className="text-xs text-muted-foreground">
              Press <kbd className="rounded bg-muted px-1.5 py-0.5">Ctrl</kbd> +
              <kbd className="ml-1 rounded bg-muted px-1.5 py-0.5">Enter</kbd> to
              generate
            </p>

            <Button
              size="lg"
              className="rounded-xl px-8"
              disabled={!prompt.trim()}
            >
              🚀 Generate Report
            </Button>
          </div>
        </div>

        {/* Example Prompts */}
        <ExamplePrompts onSelect={setPrompt} />
      </div>
    </Card>
  );
}