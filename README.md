# Customer Support Buddy

![Customer Support Buddy Banner](https://via.placeholder.com/1200x300?text=Customer+Support+Buddy)

A GPT-powered customer support assistant that leverages **LangChain**, **OpenAI**, and **Pinecone** to provide context-aware, dynamic responses. This project is designed to help streamline customer queries by integrating support documents and maintaining conversation history.

## Features
- **AI-Powered Responses:** Utilizes GPT for natural language understanding and response generation.
- **Contextual Support:** Retrieves relevant support documents using Pinecone.
- **Conversation History:** Persists user interactions with SQLite.
- **Interactive CLI:** Easy-to-use command line interface for real-time support.

## Tech Stack
- **Language:** Python
- **Libraries:** LangChain, OpenAI, Pinecone, SQLite
- **Deployment:** Local & cloud-friendly

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/customer_support_buddy.git
   cd customer_support_buddy
2. **Setup a virutal Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependecies:**
   ```bash
   pip install -r requirements.txt
4. **Configure Environment Variables:**
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   export PINECONE_API_KEY=your_pinecone_api_key
   export PINECONE_ENV=your_pinecone_env

Usage
Run the assistant with:
```bash
python customer_support_buddy.py
Type your queries in the terminal. Type exit to end the session.
```

Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

License
Distributed under the MIT License. See LICENSE for details.

Contact
Rachna Pandya - LinkedIn | Email
GitHub: rachnapandya


