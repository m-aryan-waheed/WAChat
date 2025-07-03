#ChatWA - Flask AI Chatbot

Overview

ChatWA is a web-based AI chatbot built with Flask and vanilla HTML, CSS, and JavaScript. It connects to the Deepseek model via OpenRouter.ai to generate conversational responses. The app includes features like syntax highlighting for code snippets, copy-to-clipboard buttons, a conversation history sidebar, a responsive layout that works well on both desktop and mobile devices, and speech-to-text input using a microphone. The frontend uses Marked.js to render Markdown and Highlight.js for code highlighting, which creates a smooth and interactive chat experience.

#Installation

To install and run the project, you first need to clone the repository and navigate into the project folder. You can optionally create and activate a Python virtual environment by using the command python3 -m venv venv and then source venv/bin/activate on macOS or Linux, or by running python -m venv venv followed by venv\Scripts\activate on Windows.

Once your environment is ready, you should install the required Python dependencies using the command pip install flask requests.

#API Key

You will need an API key from OpenRouter.ai to use the AI backend. For security reasons, you should not hard-code this key directly into your code. Instead, it’s best to store it as an environment variable so it stays private and safe.

#Running the App

After you’ve configured your API key, you can start the Flask server by running the command python app.py. Then you can open your web browser and visit http://localhost:5000 to start using the chatbot.

#How It Works

When you send a message in the chat interface, the frontend makes a POST request to the Flask backend at the /api/ai/chat endpoint. The backend forwards your message to OpenRouter’s Deepseek model and returns the AI’s response. The chatbot then displays the response in the interface with Markdown formatting and syntax highlighting, including handy copy buttons for any code snippets that appear.
