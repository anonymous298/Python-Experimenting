import os
import streamlit as st

from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

# Building our streamlit application
st.title('RAG Chat Application Using Ollama Models')
st.write('Input your web link and start chatting with it...')

url = st.text_input('Enter the web link')

if url:
    # Loading the documents from web
    st.session_state.loader = WebBaseLoader(url)
    st.session_state.docs = st.session_state.loader.load()

    # Splitting the documents into chunks
    st.session_state.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.documents = st.session_state.splitter.split_documents(st.session_state.docs)

    # Creating Local Vector Store
    st.session_state.embedding = OllamaEmbeddings(model='mxbai-embed-large:335m')
    st.session_state.vectorstore = Chroma.from_documents(documents=st.session_state.documents, embedding=st.session_state.embedding)

    # Creating our Retriever
    st.session_state.retriever = st.session_state.vectorstore.as_retriever()

    # Creating our prompt template 
    st.session_state.template = """Answer the question based only on the following context:

    {context}

    Question: {input}
    """

    st.session_state.prompt = ChatPromptTemplate.from_messages(
        [
            ('system', 'You are an helpful assistant I am giving you the context reply the user according to the context'),
            ('user', st.session_state.template)
        ]
    )

    # Creating our Retrieval Chain
    st.session_state.llm = ChatOllama(model='llama3.2:3b')

    st.session_state.document_chain = create_stuff_documents_chain(st.session_state.llm, st.session_state.prompt)

    st.session_state.retrievalchain = create_retrieval_chain(st.session_state.retriever, st.session_state.document_chain)

    user_input = st.chat_input('Enter what you want to chat with URL')

    if user_input:
        st.session_state.response = st.session_state.retrievalchain.invoke(
            {'input' : user_input}
        )

        with st.chat_message('user'):
            st.write(user_input)

        with st.chat_message('assistant'):
            st.write(st.session_state.response['answer'])


else:
    st.warning('Please input your Web URL')