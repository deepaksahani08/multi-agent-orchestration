export type WorkflowStatus =
  | "pending"
  | "running"
  | "completed"
  | "failed";

export interface AgentStatus {
  name: string;

  status:
    | "pending"
    | "running"
    | "completed"
    | "failed";

  duration_ms?: number;

  progress?: number;
}

export interface GenerateRequest {
  query: string;
}

export interface GenerateResponse {
  query: string;

  plan: {
    goal: string;
    tasks: string[];
  };

  research: {
    summary: string;
    findings: string[];
    sources: string[];
  };

  analysis: {
    insights: string[];
    trends: string[];
    opportunities: string[];
    risks: string[];
    recommendations: string[];
  };

  report: {
    markdown: string;
  };

  agent_status: AgentStatus[];
}