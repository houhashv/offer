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
