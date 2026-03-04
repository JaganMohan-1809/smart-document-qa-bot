import streamlit as st
from pdf_reader import extract_text_from_pdf
from llm import ask_llm
from logger import setup_logger

logger = setup_logger()

st.set_page_config(page_title="Document Q&A Bot")

st.title("📄 Smart Document Q&A Bot")

st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])


if uploaded_file:

    logger.info("PDF uploaded by user")

    with st.spinner("Reading document..."):

        document_text = extract_text_from_pdf(uploaded_file)

    st.success("Document loaded successfully")

    question = st.text_input("Ask a question")

    if question:

        logger.info(f"User question: {question}")

        with st.spinner("Generating answer..."):

            answer = ask_llm(document_text, question)

        st.subheader("Answer")

        st.write(answer)

        logger.info("Answer displayed to user")