  import { create } from "zustand";

  import { reportService } from "@/services/report-service";
  import type {
    AgentStatus,
    GenerateResponse,
  } from "@/types/report";

  interface WorkflowStore {
    // State
    prompt: string;
    loading: boolean;
    error: string | null;

    report: string;
    workflow: AgentStatus[];

    response: GenerateResponse | null;

    // Actions
    setPrompt: (prompt: string) => void;

    reset: () => void;

    generateReport: () => Promise<void>;
  }

  const delay = (ms: number) =>
    new Promise((resolve) => setTimeout(resolve, ms));

  export const useWorkflowStore = create<WorkflowStore>((set, get) => ({
    // --------------------
    // Initial State
    // --------------------

    prompt: "",

    loading: false,

    error: null,

    report: "",

    workflow: [],

    response: null,

    // --------------------
    // Actions
    // --------------------

    setPrompt: (prompt) =>
      set({
        prompt,
      }),

    reset: () =>
      set({
        prompt: "",
        loading: false,
        error: null,
        report: "",
        workflow: [],
        response: null,
      }),


    generateReport: async () => {
      const { prompt } = get();

      if (!prompt.trim()) return;

      set({
        loading: true,
        error: null,
        report: "",
        workflow: [
          {
            name: "Planner",
            status: "pending",
          },
          {
            name: "Research",
            status: "pending",
          },
          {
            name: "Analysis",
            status: "pending",
          },
          {
            name: "Report",
            status: "pending",
          },
        ],
      });

      // Helper function
      const runAgent = async (name: string) => {
        // Running
        set((state) => ({
          workflow: state.workflow.map((agent) =>
            agent.name === name
              ? { ...agent, status: "running" }
              : agent
          ),
        }));

        await delay(700);

        // Completed
        set((state) => ({
          workflow: state.workflow.map((agent) =>
            agent.name === name
              ? { ...agent, status: "completed" }
              : agent
          ),
        }));
      };

      try {
        // 🚀 Start backend request immediately
        const apiPromise = reportService.generate({
          query: prompt,
        });

        // 🎬 Animate workflow while backend is working
        await runAgent("Planner");
        await runAgent("Research");
        await runAgent("Analysis");
        await runAgent("Report");

        // Wait for backend
        const response = await apiPromise;

        set({
          loading: false,
          response,
          report: response.report.markdown,
          workflow:
            response.agent_status.length > 0
              ? response.agent_status
              : get().workflow,
        });
      } catch (error) {
        set({
          loading: false,
          error:
            error instanceof Error
              ? error.message
              : "Something went wrong.",
        });
      }
    },
  }));