from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

# Initialize FastAPI
app = FastAPI()

# Initialize OpenAI client
client = OpenAI(api_key="TOKEN_GOES_HERE")

# Function to call OpenAI API for chat completion
def get_openai_response(prompt):
    try:
        # Create a chat completion request using the new client method
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        # Return the response content
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"

# Define the request model
class QueryRequest(BaseModel):
    question: str

# Read the knowledge base from the text file
def read_knowledge_base():
    try:
        with open("knowledge_base.txt", "r") as file:
            return file.read()
    except Exception as e:
        return f"Error reading knowledge base: {str(e)}"

# Endpoint to answer questions based on RAG learning data
@app.post("/ask/")
async def ask_question(request: QueryRequest):
    question = request.question
    
    # Read the knowledge base data
    context = read_knowledge_base()
    
    if "Error" in context:
        return {"error": context}
    
    # Construct the prompt with the context and the user's question
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"

    # Call OpenAI API to get the response
    answer = get_openai_response(prompt)

    return {"answer": answer}