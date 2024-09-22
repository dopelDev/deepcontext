# deepContext Structure

```plaintext
deepcontext_lsp/
├── __init__.py                       # Inicializa el módulo DeepContext y ejecuta los tests de integración
├── .gitignore                        # Files Blacklist 
├── features/                         # Módulo que agrupa las funcionalidades LSP
│   ├── __init__.py                   # Inicializa el módulo de funcionalidades
│   ├── completion.py                 # Autocompletado (textDocument/completion)
│   ├── hover.py                      # Hover (textDocument/hover)
│   ├── definition.py                 # Definición (textDocument/definition)
│   ├── references.py                 # Referencias (textDocument/references)
│   ├── rename.py                     # Renombrar (textDocument/rename)
│   ├── signature_help.py             # Ayuda de Signaturas (textDocument/signatureHelp)
│   ├── diagnostics.py                # Diagnósticos (textDocument/publishDiagnostics)
│   ├── formatting.py                 # Formato de código (textDocument/formatting)
│   ├── code_action.py                # Code Actions (textDocument/codeAction)
│   ├── code_lens.py                  # Code Lens (textDocument/codeLens)
│   ├── workspace_symbol.py           # Símbolos del Espacio de Trabajo (workspace/symbol)
│   └── semantic_tokens.py            # Tokens Semánticos (textDocument/semanticTokens)
├── tests/                            # Carpeta para las pruebas de PyTest
│   ├── __init__.py                   # Inicializa el paquete de pruebas
│   ├── test_completion.py            # PyTest para Autocompletado
│   ├── test_hover.py                 # PyTest para Hover
│   ├── test_definition.py            # PyTest para Definición
│   ├── test_references.py            # PyTest para Referencias
│   ├── test_rename.py                # PyTest para Renombrar
│   ├── test_signature_help.py        # PyTest para Ayuda de Signaturas
│   ├── test_diagnostics.py           # PyTest para Diagnósticos
│   ├── test_formatting.py            # PyTest para Formato de Código
│   ├── test_code_action.py           # PyTest para Code Actions
│   ├── test_code_lens.py             # PyTest para Code Lens
│   ├── test_workspace_symbol.py      # PyTest para Símbolos del Espacio de Trabajo
│   └── test_semantic_tokens.py       # PyTest para Tokens Semánticos
├── ollama/                           # Módulo para las interacciones con Ollama
│   ├── __init__.py                   # Inicializa el módulo Ollama
│   ├── ollama_client.py              # Cliente para hacer llamadas al servidor de Ollama
│   ├── integration_test.py           # Test de integración para verificar el servidor Ollama
│   └── ollama.env                    # Configuración de entorno del servidor Ollama
├── docs/                             # Documentación adicional
│   ├── usage.md                      # Instrucciones de uso del proyecto
│   ├── configuration.md              # Detalles de configuración del proyecto
│   ├── development.md                # Guía de desarrollo para colaboradores
│   ├── LICENSE.md                    # Licencia del proyecto
│   ├── README.md                     # Resumen y visión general del proyecto
│   ├── structure.md                  # Estructura de carpetas y archivos en formato Markdown
│   └── structure.json                # Estructura de carpetas y archivos en formato JSON
```

- neovim: Configuraciones y scripts relacionados con la configuración de Neovim.
  - init.lua: Archivo de configuración principal para Neovim.
  - lua: Directorio que contiene módulos específicos de Lua para funcionalidades como autocompletado, refactorización, optimización, documentación, y texto a voz (TTS).

- doppelganger: Contiene scripts y herramientas para el análisis y verificación del código.
  - shadow: Implementaciones en Python para diferentes funcionalidades del servidor LSP.
  - pytest: Directorio de pruebas utilizando pytest para verificar la funcionalidad del código.
    - test_shadow: Pruebas para los scripts en el directorio shadow.
    - test_server_requests: Pruebas que verifican los endpoints y el rendimiento del servidor.


- scripts: Scripts de bash para tareas administrativas y de configuración.
  - install_dependencies.sh: Instala las dependencias necesarias para el proyecto.
  - setup_neovim.sh: Configura el entorno de Neovim.
  - start_server.sh: Script para iniciar el servidor LSP.


- docs: Documentación del proyecto.
  - usage.md: Instrucciones de uso del proyecto.
  - configuration.md: Detalles sobre cómo configurar el proyecto.
  - development.md: Información para desarrolladores sobre cómo contribuir al proyecto.

- env: Contiene el entorno virtual de Python donde se gestionan todas las dependencias necesarias para el proyecto.

- LICENSE: Archivo de licencia del proyecto que especifica los términos bajo los cuales se distribuye el software.

- README.md: Archivo de documentación principal que proporciona una descripción general del proyecto.

- .gitignore: Lista de archivos y directorios que deben ser ignorados por Git.

**UPDATE:**
Thursday 12 Sep

**server_config.env**:
_Para facilitar la configuracion del server y los models_

**UPDATE**
Sunday 22 September
**Restructuracion General**

_REMOVE_:
* Infraestructura de Lua
* TTS Features
