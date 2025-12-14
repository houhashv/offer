import sys
import argparse
from config import Config
from team_agents.orchestrator import Orchestrator
from utils.input_parser import read_file
from utils.logger import logger
from rich.console import Console

console = Console()

def main():
    # Validate configuration before proceeding
    Config.validate()
    
    parser = argparse.ArgumentParser(description="Multi-Agent Pricing Proposal System")
    parser.add_argument("input_file", help="Path to the input file (md, txt, pdf, docx)")
    args = parser.parse_args()

    try:
        logger.info(f"Starting application with input file: {args.input_file}")
        console.print(f"[bold blue]Reading input file: {args.input_file}[/bold blue]")
        content = read_file(args.input_file)
        
        orchestrator = Orchestrator()
        orchestrator.run_proposal_generation(content)
        
        logger.info("Proposal generation successful.")
        console.print("[bold green]Success! Proposal generated at 'proposal.md'[/bold green]")
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}", exc_info=True)
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
