"use client";

import { Card } from "@/components/ui/card";

import { workflowSteps } from "../types";
import { WorkflowCard } from "./WorkflowCard";

export function WorkflowPanel() {
  return (
    <Card className="glass-card rounded-3xl p-6">
      <div className="mb-5">
        <h2 className="text-xl font-bold">
          AI Workflow
        </h2>

        <p className="mt-2 text-sm text-muted-foreground">
          Specialized AI agents collaborate to produce
          a professional report.
        </p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        {workflowSteps.map((step) => (
          <WorkflowCard
            key={step.id}
            title={step.title}
            description={step.description}
            icon={step.icon}
            status={step.status}
            color={step.color}
          />
        ))}
      </div>
    </Card>
  );
}