# Ai API INTEGRATION PROJECT
## Project Description
This project demonstrates how to integrate multiple AI APIs using Python.
Each program takes user input, sends it to an AI model, and displays the response.
The APIs used in this project are:
Groq

Cohere

Hugging Face

Google Gemini

Ollama (local AI)

# Setup Instructions

1. Clone the repository

git clone https:github.com/saikiran-esk/assignment
cd assignment-3

3. Install dependencies
pip install -r requirements.txt

# How to Obtain API Keys

1. Groq

Visit: https://console.groq.com/

Generate API key

set GROQ_API_KEY="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"

2. Cohere

Visit: https://dashboard.cohere.com/

Generate API key

set COHERE_API_KEY="Jz4OVsjTr96qLD4EvVtLvmbxhrrjHm8M56A3WmzI"

3. Hugging Face

Visit: https://huggingface.co/settings/tokens

Create token (enable inference access)

set HUGGINGFACE_API_KEY="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"

4. Google Gemini

Visit: https://makersuite.google.com/app/apikey

Generate API key

set GEMINI_API_KEY="AIzaSyD9yw7DW-Li2XMmw-3PO3EqoWvu6EEwbng"

5. Ollama (No API Key Required)

Install Ollama: https://ollama.com/

Run a model locally:

ollama run tinyllama

# How to run each Program

Run each file individually:

python openai_api.py

python groq_api.py

python cohere_api.py

python huggingface_api.py

python gemini_api.py

python ollama_api.py

Each program:

Accepts user input

Sends request to API

Displays response

# Screenshots

Screenshots of working outputs are stored in the screenshots/ folder.

Examples:


Groq output

Cohere output

Hugging Face output

Gemini output

Ollama output

# Project Structure

assignment-3/ 
|

├── openai_api.py 

├── groq_api.py 

├── cohere_api.py 

├── huggingface_api.py 

├── gemini_api.py 

├── ollama_api.py

│

├── requirements.txt 

├── README.md 

└── screenshots/


# Features

Uses environment variables for API keys (secure)

Supports multiple AI providers

Simple command-line interface

Includes error handling

