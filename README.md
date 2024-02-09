# Tree Parser Test Task

## Installation and Setup

- git clone https://github.com/BloodScore/tree-parser.git
- pip install -r requirements.txt

## Run App

- uvicorn src.main:app 

## Testing

- curl -X POST http://localhost:8000/api/parse_tree -H 'Content-Type: application/json' (or application/xml) -d "\<tree>"