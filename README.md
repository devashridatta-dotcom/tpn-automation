TPN Automation
Automated License Intelligence and Compliance Risk Analysis from Third‑Party Notices (TPN) Documents.
Overview
TPN Automation extracts, analyzes, and classifies license information contained in Third‑Party Notice (TPN) documents.
This system is designed to support engineering, legal, and compliance teams by providing automated processing of vendor‑supplied TPN PDFs.
The framework helps to:

Parse and extract components from TPN PDFs
Normalize license names and metadata
Identify compliance risks
Produce structured outputs for downstream systems
Reduce manual effort and human error

Features

TPN PDF/Text Parsing
License Detection and Normalization
Risk Scoring Engine
Structured Output in CSV/JSON formats
Automated Test Suite
Modular and Extensible Architecture

Project Structure
tpn_automation/
│
├── src/                      
│   └── tpn_automation/
│       ├── __init__.py
│       ├── main.py
│       ├── parser.py
│       ├── risk.py
│       ├── utils.py
│
├── tests/                    
│   ├── test_basic_parse.py
│   ├── test_import.py
│   └── sample_tpn.pdf
│
├── docs/                     
│   ├── architecture.md
│   ├── usage.md
│   └── contributing.md
│
├── scripts/                  
├── data/                     
├── notebooks/                
│
├── LICENSE
├── README.md
└── .gitignore

Getting Started
1. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

2. Install dependencies
If using Poetry:
poetry install

If using pip:
pip install -r requirements.txt

Usage
Command Line
python -m tpn_automation.main \
  --input data/sample_tpn.pdf \
  --output output.json

Programmatic Example
Pythonfrom tpn_automation.parser import parse_tpnfrom tpn_automation.risk import score_riskcomponents = parse_tpn("sample_tpn.pdf")risk_report = score_risk(components)print(risk_report)Show more lines
Running Tests
pytest

Documentation
Documentation is provided in the docs/ directory:

architecture.md
usage.md
contributing.md

Contributing
Contributions are welcome.
Please open an issue or submit a pull request.
License
This project is licensed under the terms of the LICENSE file included in the repository.
