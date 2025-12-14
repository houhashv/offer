"""
CEO Meta-Agent that orchestrates specialist agents using the Manager pattern.
The CEO agent treats specialist agents as tools and coordinates the proposal generation.
"""
from agents import Agent
from config import Config
from team_agents.staff import (
    create_fullstack_developer,
    create_devops_engineer,
    create_security_specialist,
    create_data_scientist,
    create_data_engineer,
)


def create_ceo_agent() -> Agent:
    """
    Create the CEO meta-agent that orchestrates all specialist agents.
    
    The CEO agent uses the Manager (agents as tools) pattern where specialist
    agents are exposed as callable tools. The CEO decides when to consult each
    specialist and synthesizes their responses into a comprehensive proposal.
    
    Returns:
        Agent: Configured CEO meta-agent with specialist agents as tools
    """
    # Create all specialist agents
    fullstack_dev = create_fullstack_developer()
    devops = create_devops_engineer()
    security = create_security_specialist()
    data_scientist = create_data_scientist()
    data_engineer = create_data_engineer()
    
    # Create CEO agent with specialists exposed as tools
    ceo_instructions = Config.get_ceo_prompt()
    ceo_agent = Agent(
        name="CEO",
        model=Config.LLM_MODEL,
        instructions=ceo_instructions,
        tools=[
            fullstack_dev.as_tool(
                tool_name="fullstack_expert",
                tool_description="Consult the Full Stack Developer for technical development analysis, architecture, and implementation estimates.",
            ),
            devops.as_tool(
                tool_name="devops_expert",
                tool_description="Consult the DevOps Engineer for infrastructure, deployment, CI/CD, and cloud cost analysis.",
            ),
            security.as_tool(
                tool_name="security_expert",
                tool_description="Consult the Security Specialist for security requirements, compliance, and risk mitigation.",
            ),
            data_scientist.as_tool(
                tool_name="datascience_expert",
                tool_description="Consult the Data Scientist for AI/ML requirements and data analysis needs.",
            ),
            data_engineer.as_tool(
                tool_name="dataeng_expert",
                tool_description="Consult the Data Engineer for data pipeline, ETL, and data storage architecture.",
            ),
        ],
    )
    
    return ceo_agent
