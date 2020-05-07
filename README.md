# Cyber Plows

UML Intro to Artificial Intelligence semester group project to compare & test different search algorithms.

Created scenario is a theoretical autonomous plow (agent) attempting to clean snow in the most efficient way possible.

The agent is given limited gas (must refuel at base) and can must relocate snow.

## Components

1. Parsing of bitmaps to usable graphs
2. Organization & Functionality of agents
3. GUI
4. Search algorithms
5. Scoring

## Requirements

`Python Version: 3.8`

### Dependencies

Dependencies are located in src/requirements.txt

```
pip install -r requirements.txt
```

## How to use

The main entry point for the project is currently:
`./main.py`

It **must be run from the src directory** due to how Python handles references to to other directories in the workspace.
