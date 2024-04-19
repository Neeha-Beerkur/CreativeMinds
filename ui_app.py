import streamlit as st
from transformers import pipeline
import os

# Set the API key for Hugging Face
os.environ["HF_HOME"] = os.getcwd()
os.environ["API_KEY"] = "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"

# Initialize the text generation pipeline
generator = pipeline("text2text-generation", model="distilgpt2")

def generate_text(prompt):
    # Generate text based on the prompt
    generated_text = generator(prompt, max_length=100, do_sample=True, temperature=0.7, truncation=True)
    return generated_text[0]['generated_text']

def main():
    st.title("Text Generation by Creative Minds")

    # Initialize session state to store history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Get user input prompt
    prompt = st.text_area("Enter your prompt here:")

    if st.button("Generate"):
        if prompt:
            # Generate text and display
            generated_text = generate_text(prompt)
            st.write(generated_text)

            # Ensure history attribute is initialized
            if "history" not in st.session_state:
                st.session_state.history = []

            # Store prompt and generated text in history
            st.session_state.history.append({"prompt": prompt, "generated_text": generated_text})

    # Display history
    st.title("History")
    for item in st.session_state.history:
        st.write(f"Prompt: {item['prompt']}")
        st.write(f"Generated Text: {item['generated_text']}")
        st.write("---")

if __name__ == "__main__":
    main()
