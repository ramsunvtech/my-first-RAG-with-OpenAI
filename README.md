# my-first-RAG-with-OpenAI
Retrieval-Augmented Generation (RAG) application built using OpenAI's API.

### FastAPI RAG Learning App with OpenAI Integration

This project implements a simple FastAPI application that answers questions based on a knowledge base stored in a text file. The app integrates with OpenAI's GPT-3.5 model to provide context-based answers using a RAG (Retrieval-Augmented Generation) approach.

## Features
- **FastAPI-based**: Provides an API to query and retrieve answers.
- **OpenAI Integration**: Uses OpenAI's API to generate responses based on a knowledge base.
- **Simple Knowledge Base**: Stores data in a plain text file for easy editing.

## Requirements

Before running the application, make sure you have the following dependencies installed:

- Python 3.7+
- FastAPI
- Uvicorn
- OpenAI Python SDK

You can install the necessary dependencies using pip:

```bash
pip install fastapi uvicorn openai
