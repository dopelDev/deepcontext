# DeepContext LSP: AI-Powered LSP Server for Neovim

## Project Overview

**DeepContext LSP** is a Language Server Protocol (LSP) server designed to integrate with Neovim, powered by Ollama's artificial intelligence. The goal is to enhance the development experience by providing advanced features like intelligent autocompletion, refactoring, code optimization, documentation generation, real-time analysis, and text-to-speech (TTS) capabilities. **DeepContext LSP** is adaptable, allowing you to adjust the AI processing level between quick responses (QUICK) and deep analysis (DEEP). It is optimized for local networks, so no HTTPS protection is required, making setup easy and efficient.

## Software Prerequisites

Before installing and configuring **DeepContext LSP**, ensure your environment meets the following software requirements:

- **Neovim**: Version **v0.10.1** or higher.
- **LuaJIT**: Version **2.1.1713484068** or higher.
- **Python**: Version **3.11** or higher.
- **Ollama AI Server**: Installed and configured on a local server machine.
- **LuaRocks**: Package manager for Lua.
- **LuaFileSystem (lfs)**: Library for file and directory manipulation.
- **lua-websockets**: Library for WebSockets handling (if using streaming connection).
- **dkjson**: Library for JSON manipulation in Lua.
- **eSpeak**: Text-to-Speech engine installed on the system.
- **Pytest**: Testing tool for Python.

## Key Features

### 1. Intelligent Autocompletion and Real-Time Suggestions

DeepContext LSP uses advanced AI models to provide context-based autocompletion. Real-time suggestions help developers write code faster and with fewer errors, improving productivity and reducing development time.

### 2. Automatic Documentation Generation

DeepContext LSP can automatically generate detailed comments and documentation for your code, making it easier to maintain the project and ensuring that the code is well-documented and easy to understand for other developers.

### 3. Context-Based Code Analysis

The tool offers detailed analysis at the project, module, file, and code block levels. This capability provides more relevant and specific suggestions, helping developers understand the impact of changes and identify potential problems before they become critical errors.

### 4. Flexible Processing Level Configuration

Developers can choose between "QUICK" processing modes for fast, lightweight responses or "DEEP" modes for comprehensive, detailed code analysis. This flexibility allows users to adjust the level of detail according to project needs.

### 5. Optimization for Local Networks

DeepContext LSP is designed to work in local network environments without requiring HTTPS protection, ideal for development teams working on secure internal networks. This simplifies setup and reduces network overhead, improving performance.

### X. Streaming Connection with WebSockets(TBD)

DeepContext LSP can use WebSockets to provide a persistent, bidirectional connection, improving the efficiency of real-time feedback. This reduces latency and allows for smoother interaction between the code editor and the LSP server.

## Installation and Setup

1. **Install Dependencies:**
   - Use LuaRocks to install `luafilesystem`, `lua-websockets(TBD)`, and `dkjson`.
   - Install `pytest` for Python testing.

2. **Configure Neovim:**
   - Ensure Neovim is configured to use Lua and the installed libraries.
   - NVIM v0.11.0-dev or above

3. **Setup Ollama Server:**
   - Set up the Ollama server on a local network machine, ensuring it is accessible from Neovim clients.

## Using DeepContext LSP

- **Neovim Integration:** 
  Configure Neovim to interact with DeepContext LSP using the available functions to send analysis, suggestion requests.

- **Processing Modes:** 
  Adjust the processing level (QUICK or DEEP) according to development needs and the required level of analysis.

## Testing and Quality

- **Automated Tests:** 
  Use the Python doppelganger script along with `pytest` to run automated tests and ensure the project's functionality and reliability, including TTS features.

## Python Doppelganger Script

The Python doppelganger script is designed to create a shadow script to replica Script that mimics specific features of a target script or application.
It uses Test Driven Development (TDD) methodologies to ensure that all functionalities are accurately replicated and tested.
The Script integrates with the Pytest module for automated testing, ensuring robust validation of all replicated features.

## Future Improvements

- **Integration with more AI models:** Expand support to use different AI models depending on the project's specific needs.
- **Improved error handling and automatic reconnection:** Optimize server robustness against failures and disconnections.
- **Support for more languages and file types:** Expand support for code analysis in different programming languages and file types.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve **DeepContext LSP**.

