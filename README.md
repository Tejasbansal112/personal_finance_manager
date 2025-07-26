This project is a Python-based Personal Finance Manager, created as a stepping stone toward a fully automated financial tracking system.

It allows users to record income and expenses, categorize transactions, and receive basic financial advice powered by an AI model using the **Groq API with Llama 
Features

   Add and track income & expenses
   Categorize spending (Rent, Entertainment, Food, etc.)
   Ask basic financial questions using AI (via LLM)
   Get a summary of savings and spending
   Data stored using CSV (lightweight and local)

Technologies Used

Python
  `os`, `time` modules
  Groq’s **OpenAI-compatible LLM API**
  (Optional) CSV for transaction storage
How the AI Works

The project includes an `ai_use()` function that sends a prompt to a large language model (LLaMA3) via Groq API, which responds with basic financial advice based on the input.

Note: API key is hidden for security — you'll need to set your own in your system environment using:
bas
export my_api_python="my_actual_key"

Built by Tejas Bansal  
BBA FinTech student at NMIMS  
CFA Level 1 candidate  
Passionate about combining Finance + Tech to build real-world tools
