<div align="center">
  <img src="https://www.shkhina-ai-labs.com/assets/images/logo.png" alt="Logo" width="200">
</div>

# Multi-Agent Pricing Proposal System

An AI-powered system that generates comprehensive project proposals using a team of specialist agents coordinated by a CEO meta-agent. The system analyzes project requirements and produces detailed technical breakdowns, cost estimates, and timelines.

## ⚠️ Important Disclaimer

**The hourly rates and pricing information included in the generated proposals are EXAMPLE VALUES ONLY and should NOT be considered binding or as actual pricing quotes.** The system uses default hourly rates (configurable via environment variables) for demonstration purposes. All pricing estimates are illustrative and should be reviewed and adjusted based on your specific business requirements, market rates, and project circumstances.

## Features

- 🤖 **Multi-Agent Architecture**: Uses OpenAI Agents SDK with a CEO meta-agent pattern
- 👥 **Specialist Team**: Five domain experts (Full Stack Dev, DevOps, Security, Data Science, Data Engineering)
- 📄 **Multiple Input Formats**: Supports Markdown, TXT, PDF, and DOCX files
- 📊 **Comprehensive Proposals**: Generates detailed proposals with cost breakdowns and timelines
- 🎨 **Rich CLI**: Beautiful terminal output using the Rich library

## Architecture

The system uses a **CEO Meta-Agent Pattern** where:
- A CEO agent orchestrates the proposal generation process
- Specialist agents (Full Stack Developer, DevOps Engineer, Security Specialist, Data Scientist, Data Engineer) are exposed as tools
- The CEO consults each specialist and synthesizes their inputs into a comprehensive proposal

## Quick Start

### Prerequisites

- **Python 3.8 or higher** (check with `python --version` or `python3 --version`)
- **OpenAI API Key** - Get one from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Git** (for cloning the repository)

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd pricing
   ```

2. **Create a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   
   # macOS/Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   
   # Windows (Command Prompt)
   venv\Scripts\activate.bat
   
   # macOS/Linux
   source venv/bin/activate
   ```
   
   > **Note:** You should see `(venv)` in your terminal prompt when activated.

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   > **Note:** If you encounter issues, try `pip install --upgrade pip` first.

5. **Set up environment variables:**
   
   **On Windows:**
   ```powershell
   Copy-Item .env.example .env
   ```
   
   **On macOS/Linux:**
   ```bash
   cp .env.example .env
   ```

6. **Edit the `.env` file** and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_actual_api_key_here
   LLM_MODEL=gpt-4o
   LLM_PROVIDER=openai
   ```
   
   > **Important:** Replace `your_actual_api_key_here` with your actual OpenAI API key. Never commit the `.env` file to version control.

7. **Verify the setup:**
   ```bash
   python main.py --help
   ```
   
   If you see the help message, you're ready to go!

## Usage

### Basic Usage

Run the application with a project brief file:

```bash
python main.py <input_file>
```

**Supported file formats:**
- Markdown (`.md`)
- Text (`.txt`)
- PDF (`.pdf`)
- Word documents (`.docx`)

### Example

1. **Create a project brief file** (e.g., `my_project.md`):
   ```markdown
   # Project: E-Commerce Platform
   
   We need a modern e-commerce platform with user authentication,
   product catalog, shopping cart, and payment integration.
   ```

2. **Run the proposal generator:**
   ```bash
   python main.py my_project.md
   ```

3. **View the generated proposal:**
   The system will:
   - Read and parse your project requirements
   - Coordinate with all specialist agents
   - Generate a comprehensive proposal
   - Save the output to `proposal.md` (or the file specified in `OUTPUT_FILE`)

4. **Check the output:**
   ```bash
   # View the proposal
   cat proposal.md    # macOS/Linux
   type proposal.md   # Windows
   ```

## Project Structure

```
pricing/
├── main.py                 # Entry point
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── prompts_config.json    # Agent prompts configuration
├── team_agents/
│   ├── orchestrator.py    # Main orchestrator
│   ├── ceo_agent.py       # CEO meta-agent
│   └── staff.py           # Specialist agent factory functions
└── utils/
    ├── input_parser.py    # File reading utilities
    ├── logger.py          # Logging configuration
    └── report_generator.py # Report generation utilities
```

## Configuration

The system uses environment variables and a prompts configuration file for configuration.

### Environment Variables

All configuration is done through the `.env` file. See `.env.example` for the template. Available options:

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | **Yes** | - |
| `LLM_MODEL` | Model to use | No | `gpt-4o` |
| `LLM_PROVIDER` | LLM provider | No | `openai` |
| `HOURLY_RATE` | Hourly rate for cost estimates (example only) | No | `150` |
| `MAX_TURNS` | Maximum number of agent turns | No | `30` |
| `OUTPUT_FILE` | Output file name for generated proposal | No | `proposal.md` |
| `PROMPTS_CONFIG_FILE` | Path to prompts configuration JSON file | No | `prompts_config.json` |

> **⚠️ Reminder:** The `HOURLY_RATE` is for demonstration purposes only. Adjust it in your `.env` file to match your needs, but remember that all pricing in proposals are examples, not binding quotes.

### Prompts Configuration

Agent prompts are stored in `prompts_config.json`. You can customize the instructions for each specialist agent and the CEO agent by editing this file. The hourly rate placeholder `{hourly_rate}` will be automatically replaced with the value from `HOURLY_RATE` environment variable.

**To customize prompts:**
1. Open `prompts_config.json`
2. Edit the instructions for any agent
3. Save the file
4. Run the application - changes take effect immediately

## Troubleshooting

### Common Issues

**1. "OPENAI_API_KEY is not set!" error**
   - Make sure you've created a `.env` file from `.env.example`
   - Verify your API key is correctly set in the `.env` file (no quotes, no spaces)
   - Ensure the `.env` file is in the project root directory

**2. "Prompts config file not found" error**
   - Ensure `prompts_config.json` exists in the project root
   - Check that `PROMPTS_CONFIG_FILE` in `.env` points to the correct path

**3. Import errors or missing modules**
   - Make sure your virtual environment is activated
   - Run `pip install -r requirements.txt` again
   - Try `pip install --upgrade pip` first

**4. File not found errors**
   - Use absolute paths or ensure you're running from the project root
   - Check that the input file exists and the path is correct

**5. Permission errors (Windows)**
   - Run PowerShell as Administrator if needed
   - Check file permissions on the project directory

### Getting Help

If you encounter issues:
1. Check that all prerequisites are installed
2. Verify your `.env` file is configured correctly
3. Ensure your virtual environment is activated
4. Check the `log.log` file for detailed error messages

## Requirements

- **Python 3.8+** (tested with Python 3.8, 3.9, 3.10, 3.11, 3.12)
- **OpenAI API key** with sufficient credits
- **Internet connection** (for API calls)

### Python Dependencies

All dependencies are listed in `requirements.txt`:
- `openai-agents` - OpenAI Agents SDK
- `python-dotenv` - Environment variable management
- `pypdf` - PDF file parsing
- `python-docx` - Word document parsing
- `rich` - Terminal formatting
- `requests` - HTTP requests

## Development

### Project Structure

```
pricing/
├── main.py                 # Entry point - CLI interface
├── config.py               # Configuration management and prompts loading
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── prompts_config.json    # Agent prompts configuration
├── team_agents/
│   ├── orchestrator.py    # Main orchestrator - coordinates the process
│   ├── ceo_agent.py       # CEO meta-agent - coordinates specialists
│   └── staff.py           # Specialist agent factory functions
└── utils/
    ├── input_parser.py    # File reading utilities (md, txt, pdf, docx)
    ├── logger.py          # Logging configuration
    └── report_generator.py # Report generation utilities
```

### Running Tests

Currently, the project doesn't include automated tests. To verify the setup:

```bash
# Test configuration loading
python -c "from config import Config; Config.validate(); print('✓ Config OK')"

# Test file parsing
python -c "from utils.input_parser import read_file; print('✓ Parser OK')"
```

### Customization

**To change hourly rates:**
1. Edit `.env` file: `HOURLY_RATE=200` (or your desired rate)
2. The rate will be automatically used in all agent prompts

**To customize agent behavior:**
1. Edit `prompts_config.json`
2. Modify the `instructions` field for any agent
3. Save and run - no code changes needed

**To change output location:**
1. Edit `.env` file: `OUTPUT_FILE=my_proposal.md`
2. Proposals will be saved to the specified file

## Development

### Project Structure

```
pricing/
├── main.py                 # Entry point - CLI interface
├── config.py               # Configuration management and prompts loading
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── prompts_config.json    # Agent prompts configuration
├── team_agents/
│   ├── orchestrator.py    # Main orchestrator - coordinates the process
│   ├── ceo_agent.py       # CEO meta-agent - coordinates specialists
│   └── staff.py           # Specialist agent factory functions
└── utils/
    ├── input_parser.py    # File reading utilities (md, txt, pdf, docx)
    ├── logger.py          # Logging configuration
    └── report_generator.py # Report generation utilities
```

### Running Tests

Currently, the project doesn't include automated tests. To verify the setup:

```bash
# Test configuration loading
python -c "from config import Config; Config.validate(); print('✓ Config OK')"

# Test file parsing
python -c "from utils.input_parser import read_file; print('✓ Parser OK')"
```

### Customization

**To change hourly rates:**
1. Edit `.env` file: `HOURLY_RATE=200` (or your desired rate)
2. The rate will be automatically used in all agent prompts

**To customize agent behavior:**
1. Edit `prompts_config.json`
2. Modify the `instructions` field for any agent
3. Save and run - no code changes needed

**To change output location:**
1. Edit `.env` file: `OUTPUT_FILE=my_proposal.md`
2. Proposals will be saved to the specified file

## License

[Add your license here]

## Contributing

[Add contributing guidelines if applicable]

## Support

For issues, questions, or contributions, please open an issue on the repository.

## Support

For issues, questions, or contributions, please open an issue on the repository.
