"""
Orchestrator using OpenAI Agents SDK and CEO Meta-Agent pattern.
The CEO agent coordinates all specialist agents to generate the proposal.
"""
from agents import Runner
from config import Config
from team_agents.ceo_agent import create_ceo_agent
from rich.console import Console
from utils.logger import logger

console = Console()


class Orchestrator:
    def __init__(self):
        """Initialize the orchestrator with the CEO meta-agent."""
        self.ceo_agent = create_ceo_agent()
        logger.info("Orchestrator initialized with CEO meta-agent")
    
    def run_proposal_generation(self, project_content: str) -> str:
        """
        Orchestrates the proposal generation process using the CEO meta-agent.
        
        The CEO agent will autonomously:
        1. Consult each specialist agent as needed
        2. Gather their domain-specific analyses
        3. Synthesize a comprehensive proposal
        
        Args:
            project_content: The project requirements/brief
            
        Returns:
            str: The generated proposal in markdown format
        """
        if not project_content or not project_content.strip():
            raise ValueError("Project content cannot be empty. Please provide a valid project brief.")
        
        console.print("[bold green]Starting AI-Powered Proposal Generation...[/bold green]")
        logger.info("Starting proposal generation with CEO meta-agent")
        
        # Prepare the input message for the CEO
        user_message = (
            "Please analyze the following project requirements and create a comprehensive "
            "pricing proposal. Consult with all your specialist team members to gather their "
            "expert analysis, then synthesize their inputs into a detailed proposal.\n\n"
            f"Project Requirements:\n{project_content}"
        )
        
        console.print("[cyan]CEO Agent is coordinating with specialist team...[/cyan]")
        
        try:
            # Run the CEO agent using the Agents SDK Runner
            from config import Config
            result = Runner.run_sync(
                starting_agent=self.ceo_agent,
                input=user_message,
                max_turns=Config.MAX_TURNS,
            )
            
            logger.info("CEO agent completed proposal generation")
            console.print("[bold green]Proposal generation complete![/bold green]")
            
            # Extract the final output from the result
            if not hasattr(result, 'final_output'):
                raise ValueError("Unexpected result format from agent. Missing 'final_output' attribute.")
            
            proposal = result.final_output
            
            if not proposal or not proposal.strip():
                raise ValueError("Proposal generation returned empty content. Please check your input and try again.")
            
            # Save to file
            return self._save_proposal(proposal)
            
        except Exception as e:
            logger.error(f"Error during proposal generation: {str(e)}", exc_info=True)
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
            raise

    def _save_proposal(self, proposal: str) -> str:
        """
        Save the generated proposal to a markdown file.
        
        Args:
            proposal: The generated proposal content
            
        Returns:
            str: The proposal content
        """
        output_file = Config.OUTPUT_FILE
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(proposal)
        
        logger.info(f"Proposal saved to {output_file}")
        console.print(f"[bold green]Proposal saved to: {output_file}[/bold green]")
        
        return proposal

