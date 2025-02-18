import os
import sqlite3
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

# Set your API keys and environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-west1-gcp")

if not OPENAI_API_KEY or not PINECONE_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY and PINECONE_API_KEY environment variables.")

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index_name = "customer-support-index"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536)

index = pinecone.Index(index_name)

# Setup SQLite database for conversation history
conn = sqlite3.connect("conversation_history.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS conversation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT,
    bot_response TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def save_conversation(user_input, bot_response):
    cursor.execute("INSERT INTO conversation (user_input, bot_response) VALUES (?, ?)", (user_input, bot_response))
    conn.commit()

def query_support_documents(query):
    """
    Dummy function to simulate querying support documents.
    In a full implementation, this function would query the Pinecone index using embeddings.
    """
    return f"Relevant support content for: '{query}'"

def main():
    # Initialize OpenAI LLM
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.2)

    qa_chain = RetrievalQA.from_llm(llm, retriever=None)

    print("Customer Support Buddy - Ask your questions (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Retrieve support documents (dummy example)
        support_docs = query_support_documents(user_input)
        
        # Combine the support context with the user query for the prompt
        prompt = f"Support documents context: {support_docs}\nUser query: {user_input}\nAnswer:"
        
        # Get response from LLM
        bot_response = llm(prompt)
        print("Bot:", bot_response)
        
        # Save the conversation to the database
        save_conversation(user_input, bot_response)

if __name__ == "__main__":
    main()
