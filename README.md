# DeepContext LSP: AI-Powered LSP Server for Neovim

## Project Overview

**DeepContext LSP** is a Language Server Protocol (LSP) server designed to integrate with Neovim, powered by Ollama's artificial intelligence. The goal is to enhance the development experience by providing advanced features like intelligent autocompletion, refactoring, code optimization, documentation generation, real-time analysis, and flexible processing modes (QUICK and DEEP). **DeepContext LSP** is optimized for local networks, making setup easy and efficient without the need for HTTPS protection.

## Software Prerequisites

Before installing and configuring **DeepContext LSP**, ensure your environment meets the following software requirements:

- **Neovim**: Version **v0.10.1** or higher.
- **Python**: Version **3.11** or higher.
- **Ollama AI Server**: Installed and configured on a local server machine.
- **Pytest**: Testing tool for Python.

*Note:* Lua-related dependencies and TTS features have been removed from the recent version.

## Key Features

### 1. Intelligent Autocompletion and Real-Time Suggestions

DeepContext LSP uses advanced AI models to provide context-based autocompletion, helping developers write code faster with fewer errors and enhanced productivity.

### 2. Automatic Documentation Generation

The tool automatically generates detailed documentation, ensuring maintainability and making it easier for other developers to understand the code.

### 3. Context-Based Code Analysis

Detailed analysis is provided at the project, module, file, and code block levels, enabling relevant suggestions and helping developers identify potential issues early.

### 4. Flexible Processing Level Configuration

Choose between "QUICK" processing for lightweight responses or "DEEP" modes for comprehensive code analysis, adjusting the depth of analysis as needed.

### 5. Optimized for Local Networks

DeepContext LSP is designed to work efficiently in secure local networks without requiring HTTPS, simplifying the setup process and reducing network overhead.

## Installation and Setup

1. **Install Dependencies:**
   - Ensure `pytest` is installed for Python testing.

2. **Configure Neovim:**
   - Ensure Neovim is configured correctly to use the Python environment.

3. **Setup Ollama Server:**
   - Set up the Ollama server on a local machine accessible by Neovim clients.

## Using DeepContext LSP

- **Neovim Integration:** 
  Configure Neovim to interact with DeepContext LSP, using its features to request suggestions, refactoring, and more.

- **Processing Modes:** 
  Adjust between QUICK and DEEP processing levels based on project needs.

## Testing and Quality

- **Automated Tests:** 
  Use the Python doppelganger script with `pytest` to run automated tests, ensuring functionality and reliability.

## Contributing

Contributions are welcome! Please submit issues or pull requests to improve **DeepContext LSP**.

