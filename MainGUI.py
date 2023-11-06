import os
import gradio as gr
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from css import STYLES



# Constants
OPENAI_API_KEY = "<Your API Key"
PERSIST_DIRECTORY = "persist"
DATA_DIRECTORY = "./files/"
MODEL_NAME = "gpt-4"
use_saved_model = False

# Set the OpenAI API Key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialization
chat_history = []


def initialize_index(persist=True):
    """Initialize and return the index."""
    if persist and os.path.exists(PERSIST_DIRECTORY):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=OpenAIEmbeddings())
        return VectorStoreIndexWrapper(vectorstore=vectorstore)

    loader = DirectoryLoader(DATA_DIRECTORY)
    index_kwargs = {"persist_directory": PERSIST_DIRECTORY} if persist else {}
    return VectorstoreIndexCreator(vectorstore_kwargs=index_kwargs).from_loaders([loader])


# def chat_with_bot(query):
#     """Function to chat with the bot."""
#     global chat_history
#     result = chain({"question": query, "chat_history": chat_history})
#     chat_history.append((query, result['answer']))
#     return result['answer']

def chat_with_bot(query):
    """Function to chat with the bot."""
    global chat_history
    careful_prompt = "Please read the following question carefully and provide a detailed response: "
    result = chain({"question": careful_prompt + query, "chat_history": chat_history})
    chat_history.append((query, result['answer']))
    return result['answer']


# Initialize chain
index = initialize_index(persist=use_saved_model)
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model=MODEL_NAME),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

# Gradio UI setup
iface = gr.Interface(
    fn=chat_with_bot,
    inputs=gr.Textbox(label="Your Question", placeholder="Enter your question here..."),
    outputs=gr.Textbox(label="Bot's Response", placeholder="Bot will response here..."),
    live=False,
    description="Chat with a bot about your documents! It can Summarize, Read, Explain, or Translate for you!",
    css=STYLES
)

if __name__ == "__main__":
    iface.launch()
