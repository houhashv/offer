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
    create_legal_counsel,
    create_cfo,
    create_rnd_director,
    create_sales_director,
    create_cto,
    create_coo,
    create_hr_director,
    create_product_director,
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
    # Create all specialist agents — engineering staff
    fullstack_dev = create_fullstack_developer()
    devops = create_devops_engineer()
    security = create_security_specialist()
    data_scientist = create_data_scientist()
    data_engineer = create_data_engineer()

    # Create all specialist agents — business / executive roles
    legal_counsel = create_legal_counsel()
    cfo = create_cfo()
    rnd_director = create_rnd_director()
    sales_director = create_sales_director()
    cto = create_cto()
    coo = create_coo()
    hr_director = create_hr_director()
    product_director = create_product_director()

    # Create CEO agent with specialists exposed as tools
    ceo_instructions = Config.get_ceo_prompt()
    ceo_agent = Agent(
        name="CEO",
        model=Config.LLM_MODEL,
        instructions=ceo_instructions,
        tools=[
            # Engineering staff
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
            # Business / executive roles
            legal_counsel.as_tool(
                tool_name="legal_counsel",
                tool_description="Consult Legal Counsel for NDA structure, contract type (SOW/MSA/JV), IP carve-outs, liability cap, compliance flags, and likely counterparty redlines.",
            ),
            cfo.as_tool(
                tool_name="cfo",
                tool_description="Consult the CFO for cost-to-serve via ABC, NPV at 18% hurdle, 3 price points (Conservative/Recommended/Stretch), payment milestones, and sensitivity analysis.",
            ),
            rnd_director.as_tool(
                tool_name="rnd_director",
                tool_description="Consult the R&D Director for falsifiable success criteria, eval set design, sample-size calc (≥80% power), methodology choice (AFML/ML/agent pattern), and experimental risk register.",
            ),
            sales_director.as_tool(
                tool_name="sales_director",
                tool_description="Consult the Sales Director for Hormozi Value Equation framing, 3 price tiers (Attraction/Core/Premium), demo selection per IP-protection rules, BATNA, and objection bank.",
            ),
            cto.as_tool(
                tool_name="cto",
                tool_description="Consult the CTO for C4 architecture (Context + Containers), tech-stack decisions, server placement on the 5-server fleet, build/buy/partner per AHP, and sub-processor disclosure.",
            ),
            coo.as_tool(
                tool_name="coo",
                tool_description="Consult the COO for WBS (3 levels), 3-point estimates → PERT, CPM critical path, resource histogram (Yossi-week capacity), top-5 risks, and RACI.",
            ),
            hr_director.as_tool(
                tool_name="hr_director",
                tool_description="Consult the HR Director for staffing/capacity check — does this engagement need a hire, contractor cost, key-person risk, and impact on the canonical hiring plan (Sales → ML → DevOps).",
            ),
            product_director.as_tool(
                tool_name="product_director",
                tool_description="Consult the Product Director for JTBD framing, riskiest-hypothesis identification, MVP scope, RICE-scored backlog, match to existing 22-demo catalog, and Now/Next/Later roadmap.",
            ),
        ],
    )

    return ceo_agent
