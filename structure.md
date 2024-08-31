# Estructura del Proyecto DeepContext-LSP

```plaintext
DeepContext-LSP/
├── README.md
├── LICENSE
├── .gitignore
├── neovim/
│   ├── init.lua
│   └── lua/
│       ├── lsp.lua
│       ├── autocompletion.lua
│       ├── refactoring.lua
│       ├── optimization.lua
│       ├── documentation.lua
│       └── tts.lua
├── server/
│   ├── main.lua
│   ├── websocket.lua
│   └── utils/
│       ├── json.lua
│       ├── filesystem.lua
│       └── network.lua
├── doppelganger/
│   ├── shadow/
│   │   ├── lsp.py
│   │   ├── autocompletion.py
│   │   ├── refactoring.py
│   │   ├── optimization.py
│   │   ├── documentation.py
│   │   └── tts.py
│   └── pytest/
│       ├── test_shadow/
│       │   ├── test_lsp.py
│       │   ├── test_autocompletion.py
│       │   ├── test_refactoring.py
│       │   ├── test_optimization.py
│       │   └── test_documentation.py
│       └── test_server_requests/
│           ├── test_endpoints.py
│           └── test_performance.py
├── scripts/
│   ├── install_dependencies.sh
│   ├── setup_neovim.sh
│   └── start_server.sh
├── docs/
│   ├── usage.md
│   ├── configuration.md
│   └── development.md
└── env/  # Entorno virtual de Python

