import { AppHeader } from "./AppHeader";
import { AppSidebar } from "./AppSidebar";
import { PromptPanel } from "./PromptPanel";
import { ReportPanel } from "./ReportPanel";
import { WorkflowPanel } from "./WorkflowPanel";

export function Dashboard() {
  return (
    <div className="dashboard-bg relative isolate min-h-screen">
      {/* Background Glow Effects */}
      <div className="glow-blue" />
      <div className="glow-purple" />
      <div className="glow-yellow" />

      {/* Main Content */}
      <div className="relative z-10">
        <AppHeader />

       <main className="grid min-h-[calc(100vh-4rem)] grid-cols-[80px_minmax(0,1fr)_440px] gap-6 p-6">
          {/* Sidebar */}
          <AppSidebar />

          {/* Center Content */}
           <section className="flex flex-col gap-6">
            <div className="space-y-6">
              <PromptPanel />

              <WorkflowPanel />
            </div>
          </section>

          {/* Right Panel */}
          <section className="p-6">
            <ReportPanel />
          </section>
        </main>
      </div>
    </div>
  );
}