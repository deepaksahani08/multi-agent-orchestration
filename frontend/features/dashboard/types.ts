import {
  Brain,
  Search,
  BarChart3,
  FileText,
} from "lucide-react";

export const workflowSteps = [
  {
    id: "planner",
    title: "Planner",
    description: "Task Planning",
    color: "blue",
    icon: Brain,
    status: "pending",
  },
  {
    id: "research",
    title: "Research",
    description: "Knowledge Gathering",
    color: "purple",
    icon: Search,
    status: "pending",
  },
  {
    id: "analysis",
    title: "Analysis",
    description: "AI Insights",
    color: "orange",
    icon: BarChart3,
    status: "pending",
  },
  {
    id: "report",
    title: "Report",
    description: "Markdown Output",
    color: "emerald",
    icon: FileText,
    status: "pending",
  },
] as const;

export type WorkflowStatus =
  | "pending"
  | "running"
  | "completed"
  | "failed";