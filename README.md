# DeepContext LSP: AI-Powered LSP Server for Neovim

## Project Overview

**DeepContext LSP** is a Language Server Protocol (LSP) server designed to integrate with Neovim, powered by Ollama's artificial intelligence. The goal is to enhance the development experience by providing advanced features like intelligent autocompletion, automatic refactoring, code optimization, documentation generation, real-time analysis, and text-to-speech (TTS) capabilities. **DeepContext LSP** is adaptable, allowing you to adjust the AI processing level between quick responses (QUICK) and deep analysis (DEEP). It is optimized for local networks, so no HTTPS protection is required, making setup easy and efficient.

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

### 2. Automatic Refactoring and Code Optimization

The tool suggests automatic refactoring and optimizations to improve code quality. This includes identifying duplicate code, suggesting simplifications for complex functions, and optimizing data structures and algorithms.

### 3. Automatic Documentation Generation

DeepContext LSP can automatically generate detailed comments and documentation for your code, making it easier to maintain the project and ensuring that the code is well-documented and easy to understand for other developers.

### 4. Context-Based Code Analysis

The tool offers detailed analysis at the project, file, and code block levels. This capability provides more relevant and specific suggestions, helping developers understand the impact of changes and identify potential problems before they become critical errors.

### 5. Streaming Connection with WebSockets

DeepContext LSP can use WebSockets to provide a persistent, bidirectional connection, improving the efficiency of real-time feedback. This reduces latency and allows for smoother interaction between the code editor and the LSP server.

### 6. Flexible Processing Level Configuration

Developers can choose between "QUICK" processing modes for fast, lightweight responses or "DEEP" modes for comprehensive, detailed code analysis. This flexibility allows users to adjust the level of detail according to project needs.

### 7. Text-to-Speech (TTS) with eSpeak

DeepContext LSP integrates with **eSpeak** to provide text-to-speech (TTS) capabilities. This feature allows the server to read code suggestions or documentation aloud, enhancing accessibility and providing a more interactive development experience.

### 8. Optimization for Local Networks

DeepContext LSP is designed to work in local network environments without requiring HTTPS protection, ideal for development teams working on secure internal networks. This simplifies setup and reduces network overhead, improving performance.

### 9. Automated Testing with Python Doppelganger

To complement the development and testing of DeepContext LSP, a Python doppelganger script has been created to emulate the LSP server functionalities implemented in Lua. Automated testing is performed using `pytest`, ensuring that all functionalities behave as expected under different conditions.

## Installation and Setup

1. **Install Dependencies:**
   - Use LuaRocks to install `luafilesystem`, `lua-websockets`, and `dkjson`.
   - Install `eSpeak` on your system for TTS functionality.
   - Install `pytest` for Python testing.

2. **Configure Neovim:**
   - Ensure Neovim is configured to use Lua and the installed libraries.

3. **Setup Ollama Server:**
   - Set up the Ollama server on a local network machine, ensuring it is accessible from Neovim clients.

## Using DeepContext LSP

- **Neovim Integration:** 
  Configure Neovim to interact with DeepContext LSP using the available functions to send analysis, suggestion requests, and TTS functionality.

- **Processing Modes:** 
  Adjust the processing level (QUICK or DEEP) according to development needs and the required level of analysis.

## Text-to-Speech (TTS) with eSpeak in Lua

To use eSpeak for TTS in Lua, DeepContext LSP provides a simple interface within the Lua abstraction layer. This feature can be used to convert text output from the LSP server into speech, making it easier for developers to receive auditory feedback.

Example Lua function to use eSpeak:

```lua
function speak(text)
    local command = "espeak \"" .. text .. "\""
    os.execute(command)
end
```

## Testing and Quality

- **Automated Tests:** 
  Use the Python doppelganger script along with `pytest` to run automated tests and ensure the project's functionality and reliability, including TTS features.

## Python Doppelganger and Pytest for TTS

The Python doppelganger script also includes TTS functionality using Python bindings for eSpeak or similar libraries. Pytest is used to test this feature, ensuring consistency between the Lua and Python implementations.

Example test case for TTS in Python:

```python
import os

def test_tts():
    text = "Hello, this is a test."
    os.system(f"espeak \"{text}\"")
    # Add assertions or checks to verify TTS functionality
```

## Future Improvements

- **Integration with more AI models:** Expand support to use different AI models depending on the project's specific needs.
- **Improved error handling and automatic reconnection:** Optimize server robustness against failures and disconnections.
- **Support for more languages and file types:** Expand support for code analysis in different programming languages and file types.
- **Enhanced TTS customization:** Allow for different voices, speeds, and languages in TTS settings.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve **DeepContext LSP**.

