"use client";

import { Sparkles } from "lucide-react";

const examples = [
  {
    title: "📈 NVIDIA Market",
    prompt: "Create a market research report for NVIDIA AI in 2026.",
  },
  {
    title: "🚗 Tesla Analysis",
    prompt: "Analyze Tesla's financial performance and future outlook.",
  },
  {
    title: "🤖 OpenAI vs Claude",
    prompt: "Compare OpenAI and Anthropic AI models.",
  },
  {
    title: "⚛️ Quantum AI",
    prompt: "Research the future of Quantum Computing.",
  },
];

type ExamplePromptsProps = {
  onSelect: (prompt: string) => void;
};

export function ExamplePrompts({ onSelect }: ExamplePromptsProps) {
  return (
    <div className="space-y-4">
      {/* Heading */}
      <div className="flex items-center gap-2">
        <Sparkles className="h-4 w-4 text-primary" />

        <p className="text-sm font-medium text-muted-foreground">
          Try an example
        </p>
      </div>

      {/* Prompt Chips */}
      <div className="flex flex-wrap gap-3">
        {examples.map((example) => (
          <button
            key={example.title}
            type="button"
            onClick={() => onSelect(example.prompt)}
            className=" group rounded-full border border-white/50 bg-white/70 px-4 py-2.5 text-sm font-medium text-slate-700 shadow-sm backdrop-blur-md transition-all duration-300 hover:-translate-y-1 hover:border-primary/30  hover:bg-white  hover:shadow-lg  active:scale-95 "
          >
            {example.title}
          </button>
        ))}
      </div>
    </div>
  );
}
