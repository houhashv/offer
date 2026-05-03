"""
Specialist agent factory functions using OpenAI Agents SDK.
Each function returns a configured Agent instance for a specific domain expertise.
Prompts are loaded from prompts_config.json via Config.
"""
from agents import Agent
from config import Config


def create_fullstack_developer() -> Agent:
    """Create Full Stack Developer specialist agent."""
    prompt_data = Config.get_staff_prompt("fullstack_developer")
    return Agent(
        name="FullStackDev",
        model=Config.LLM_MODEL,
        instructions=prompt_data["instructions"],
    )


def create_devops_engineer() -> Agent:
    """Create DevOps Engineer specialist agent."""
    prompt_data = Config.get_staff_prompt("devops_engineer")
    return Agent(
        name="DevOps",
        model=Config.LLM_MODEL,
        instructions=prompt_data["instructions"],
    )


def create_security_specialist() -> Agent:
    """Create Cyber Security Specialist agent."""
    prompt_data = Config.get_staff_prompt("security_specialist")
    return Agent(
        name="Security",
        model=Config.LLM_MODEL,
        instructions=prompt_data["instructions"],
    )


def create_data_scientist() -> Agent:
    """Create Data Scientist specialist agent."""
    prompt_data = Config.get_staff_prompt("data_scientist")
    return Agent(
        name="DataScientist",
        model=Config.LLM_MODEL,
        instructions=prompt_data["instructions"],
    )


def create_data_engineer() -> Agent:
    """Create Data Engineer specialist agent."""
    prompt_data = Config.get_staff_prompt("data_engineer")
    return Agent(
        name="DataEngineer",
        model=Config.LLM_MODEL,
        instructions=prompt_data["instructions"],
    )


# ─── Business-role specialists (added 2026-05-03) ──────────────────────

def create_legal_counsel() -> Agent:
    """Legal Counsel — NDA / contracts / IP / compliance."""
    prompt_data = Config.get_staff_prompt("legal_counsel")
    return Agent(name="LegalCounsel", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])


def create_cfo() -> Agent:
    """CFO — pricing / NPV / cost-to-serve."""
    prompt_data = Config.get_staff_prompt("cfo")
    return Agent(name="CFO", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])


def create_rnd_director() -> Agent:
    """R&D Director — methodology / experiments / quality."""
    prompt_data = Config.get_staff_prompt("rnd_director")
    return Agent(name="RnDDirector", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])


def create_sales_director() -> Agent:
    """Sales Director — positioning / offer tiers / BATNA."""
    prompt_data = Config.get_staff_prompt("sales_director")
    return Agent(name="SalesDirector", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])


def create_cto() -> Agent:
    """CTO — system architecture / IS strategy."""
    prompt_data = Config.get_staff_prompt("cto")
    return Agent(name="CTO", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])


def create_coo() -> Agent:
    """COO — WBS / critical path / portfolio risk."""
    prompt_data = Config.get_staff_prompt("coo")
    return Agent(name="COO", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])


def create_hr_director() -> Agent:
    """HR Director — staffing / capacity / hiring impact."""
    prompt_data = Config.get_staff_prompt("hr_director")
    return Agent(name="HRDirector", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])


def create_product_director() -> Agent:
    """Product Director — JTBD / MVP scope / roadmap."""
    prompt_data = Config.get_staff_prompt("product_director")
    return Agent(name="ProductDirector", model=Config.LLM_MODEL, instructions=prompt_data["instructions"])
