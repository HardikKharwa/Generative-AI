from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama

ollama = ChatOllama(model="llama3.2")
systemPrompt = "Remember You are M. H. Saboo Siddik Personal chatbot. You can only talk about this institute and nothing else. M. H. Saboo Siddik is located at Byculla, Mumbai: 400 008. It is a polytechnic institute which provide diploma courses in Information Technology, Computer Engineeering, Artificial Intelligence & Machine Learning (AIML), Mechanical & Civil Engineering Department. Intake for all courses is 60 seats."

while True: 
    input_text = input("You: ")
    if input_text == "exit": break
    response = ollama.invoke(systemPrompt + "\n\n" + input_text)
    try: 
        response = response.content
    except: 
        response = str(response)
    print("MHSSP: " + response)