"use client";

import { Card } from "@/components/ui/card";

import { MarkdownPreview } from "./MarkdownPreview";
import { ReportToolbar } from "./ReportToolbar";

const fakeReport = `
# Executive Summary

The AI industry continues to grow rapidly.

## Market Overview

- NVIDIA leads the AI hardware market.
- AMD continues to gain share.
- Google focuses on TPUs.

## Key Insights

Artificial Intelligence is expected to become one of the fastest-growing industries over the next decade.

## Conclusion

Organizations investing in AI infrastructure today are likely to gain a competitive advantage.
`;

export function ReportPanel() {
  return (
    <Card className="glass-card flex h-full flex-col overflow-hidden rounded-3xl">
      <ReportToolbar />

      <div className="flex-1 overflow-y-auto">
        <MarkdownPreview content={fakeReport} />
      </div>
    </Card>
  );
}