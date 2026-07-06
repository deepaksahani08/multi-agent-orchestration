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
from langchain_core.runnables import RunnableConfig
from app.agents.analysis import AnalysisAgent
from app.agents.planner import PlannerAgent
from app.agents.report import ReportAgent
from app.agents.research import ResearchAgent
from app.schemas.agent import AgentStatus
from app.schemas.workflow import WorkflowState

from app.agents.guardrail import GuardrailAgent
from app.schemas.guardrail import GuardrailCategory
# from langsmith import traceable


# ----------------------------------------------------
# Agent Instances
# ----------------------------------------------------

planner_agent = PlannerAgent()
research_agent = ResearchAgent()
analysis_agent = AnalysisAgent()
report_agent = ReportAgent()
guardrail = GuardrailAgent()



# ----------------------------------------------------
# Gauirdrail Node
# ----------------------------------------------------

def guardrail_node(state: WorkflowState, config: RunnableConfig,) -> WorkflowState:
    """
    Guardrail Node

    Reads:
        - query

    Writes:
        - guardrail
        - agent_status
    """

    _ = config

    result = guardrail.run(
        query=state.query,
    )

    state.guardrail = result

    state.agent_status.append(
        AgentStatus(
            name="Guardrail",
            status="completed",
        )
    )

    return state



# ----------------------------------------------------
# Planner Node
# ----------------------------------------------------



# @traceable(run_type="chain", name="Planner Node")
def planner_node(state: WorkflowState, config: RunnableConfig,) -> WorkflowState:
   
    """Generate the execution plan."""
    _ = config

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
# @traceable(run_type="chain", name="Research Node")
def research_node(state: WorkflowState,config: RunnableConfig,) -> WorkflowState:
    """Collect research information."""
    _ = config

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

# @traceable(run_type="chain", name="Analysis Node")
def analysis_node(state: WorkflowState, config: RunnableConfig) -> WorkflowState:
    """Analyze research findings."""
    _ = config

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

# @traceable(run_type="chain", name="Report Node")
def report_node(state: WorkflowState, config: RunnableConfig) -> WorkflowState:
    """Generate the final report."""
    _ = config

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
