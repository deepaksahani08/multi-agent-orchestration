"""
LangGraph Nodes

Each node is responsible for executing one agent and updating the shared
WorkflowState.

Nodes DO NOT contain business logic.

Business logic lives inside the agents.

Nodes simply:
    1. Read WorkflowState
    2. Execute an agent
    3. Update WorkflowState
    4. Return WorkflowState
"""

from app.agents.analysis import AnalysisAgent
from app.agents.planner import PlannerAgent
from app.agents.report import ReportAgent
from app.agents.research import ResearchAgent
from app.schemas.agent import AgentStatus
from app.schemas.workflow import WorkflowState

# ----------------------------------------------------
# Agent Instances
# ----------------------------------------------------

planner_agent = PlannerAgent()
research_agent = ResearchAgent()
analysis_agent = AnalysisAgent()
report_agent = ReportAgent()


# ----------------------------------------------------
# Planner Node
# ----------------------------------------------------


def planner_node(state: WorkflowState) -> WorkflowState:
   
    """Generate the execution plan."""

    state.agent_status.append(
        AgentStatus(name="Planner", status="running")
    )

    state.plan = planner_agent.run(
        query=state.query,
        
        )
    
    state.agent_status[-1].status = "completed"

    return state


# ----------------------------------------------------
# Research Node
# ----------------------------------------------------

def research_node(state: WorkflowState) -> WorkflowState:
    """Collect research information."""

    state.agent_status.append(
        AgentStatus(
            name="Research",
            status="running",
        )
    )

    state.research = research_agent.run(
        goal=state.plan.goal,
        tasks="\n".join(state.plan.tasks),
    )

    state.agent_status[-1].status = "completed"

    return state

# ----------------------------------------------------
# Analysis Node
# ----------------------------------------------------


def analysis_node(state: WorkflowState) -> WorkflowState:
    """Analyze research findings."""

    state.agent_status.append(
        AgentStatus(
            name="Analysis",
            status="running",
        )
    )

    state.analysis = analysis_agent.run(
        summary=state.research.summary,
        findings="\n".join(state.research.findings),
    )

    state.agent_status[-1].status = "completed"

    return state


# ----------------------------------------------------
# Report Node
# ----------------------------------------------------


def report_node(state: WorkflowState) -> WorkflowState:
    """Generate the final report."""

    state.agent_status.append(
        AgentStatus(
            name="Report",
            status="running",
        )
    )

    state.report = report_agent.run(
        goal=state.plan.goal,
        summary=state.research.summary,
        findings="\n".join(state.research.findings),
        insights="\n".join(state.analysis.insights),
        trends="\n".join(state.analysis.trends),
        opportunities="\n".join(state.analysis.opportunities),
        risks="\n".join(state.analysis.risks),
        recommendations="\n".join(state.analysis.recommendations),
    )

    state.agent_status[-1].status = "completed"

    return state
