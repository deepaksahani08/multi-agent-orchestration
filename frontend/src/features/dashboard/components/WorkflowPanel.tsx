"use client";

import { Card } from "@/components/ui/card";

import { workflowSteps } from "../types";
import { WorkflowCard } from "./WorkflowCard";

import { useWorkflowStore } from "@/store/workflow-store";

export function WorkflowPanel() {
  const { workflow } = useWorkflowStore();

  return (
    <Card className="glass-card rounded-3xl p-6">
      <div className="mb-5">
        <h2 className="text-xl font-bold">
          AI Workflow
        </h2>

        <p className="mt-2 text-sm text-muted-foreground">
          Specialized AI agents collaborate to generate your report.
        </p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        {workflowSteps.map((step) => {
          const agent = workflow.find(
            (item) =>
              item.name.toLowerCase() ===
              step.title.toLowerCase()
          );

          return (
            <WorkflowCard
              key={step.id}
              title={step.title}
              description={step.description}
              icon={step.icon}
              color={step.color}
              status={agent?.status ?? "pending"}
            />
          );
        })}
      </div>
    </Card>
  );
}