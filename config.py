import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
    
    # Agent configuration
    HOURLY_RATE = os.getenv("HOURLY_RATE", "150")
    MAX_TURNS = int(os.getenv("MAX_TURNS", "30"))
    OUTPUT_FILE = os.getenv("OUTPUT_FILE", "proposal.md")
    PROMPTS_CONFIG_FILE = os.getenv("PROMPTS_CONFIG_FILE", "prompts_config.json")
    
    # Load prompts configuration
    _prompts_config = None
    
    @classmethod
    def load_prompts_config(cls):
        """Load prompts configuration from JSON file."""
        if cls._prompts_config is None:
            config_path = Path(cls.PROMPTS_CONFIG_FILE)
            if not config_path.exists():
                raise FileNotFoundError(
                    f"Prompts config file not found: {cls.PROMPTS_CONFIG_FILE}\n"
                    f"Please ensure the file exists in the project root."
                )
            
            with open(config_path, 'r', encoding='utf-8') as f:
                cls._prompts_config = json.load(f)
        
        return cls._prompts_config
    
    @classmethod
    def get_staff_prompt(cls, role: str) -> dict:
        """Get staff prompt configuration for a specific role."""
        config = cls.load_prompts_config()
        role_key = role.lower().replace(" ", "_")
        
        if role_key not in config.get("staff_prompts", {}):
            raise ValueError(f"Unknown staff role: {role}. Available roles: {list(config.get('staff_prompts', {}).keys())}")
        
        prompt_data = config["staff_prompts"][role_key].copy()
        # Replace hourly_rate placeholder
        prompt_data["instructions"] = prompt_data["instructions"].format(hourly_rate=cls.HOURLY_RATE)
        
        return prompt_data
    
    @classmethod
    def get_ceo_prompt(cls) -> str:
        """Get CEO agent prompt."""
        config = cls.load_prompts_config()
        return config.get("ceo_prompt", {}).get("instructions", "")
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        # Check if API key is missing or empty (handles None, empty string, or whitespace-only)
        if not cls.OPENAI_API_KEY or not cls.OPENAI_API_KEY.strip():
            print("ERROR: OPENAI_API_KEY is not set!", file=sys.stderr)
            print("\nPlease set your OpenAI API key:", file=sys.stderr)
            print("1. Copy .env.example to .env", file=sys.stderr)
            print("2. Edit .env and add: OPENAI_API_KEY=your_api_key_here", file=sys.stderr)
            print("\nYou can get an API key from: https://platform.openai.com/api-keys", file=sys.stderr)
            sys.exit(1)
        
        # Validate prompts config file exists
        try:
            cls.load_prompts_config()
        except FileNotFoundError as e:
            print(f"ERROR: {str(e)}", file=sys.stderr)
            sys.exit(1)
    
    # You can add more configuration for other providers here
    # e.g., ANTHROPIC_API_KEY, etc.
