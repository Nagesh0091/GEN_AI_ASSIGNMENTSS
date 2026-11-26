import streamlit as st
from google import genai

# SET THE PAGE TITLE AND ICON
st.set_page_config(page_title="AI Greeting Card Assistant", page_icon="💌")

# GET THE GEMINI API KEY FROM STREAMLIT SECRETS
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("Gemini API key not found. Please add it to secrets.toml.")
    st.stop()

# CONFIGURE THE GEMINI API
client = genai.Client(api_key=api_key)

# MODEL NAME
MODELS = "gemini-3.5-flash-lite"


# TO SEND ANY PROMPT TO GEMINI AND RETURN THE TEXT
def ask_gemini(prompt):
    response = client.models.generate_content(model=MODELS, contents=prompt)
    return response.text


# TO LET THE AI WRITE THE PROMPT THEN USE THAT PROMPT TO WRITE THE MESSAGE
def ai_prompt_then_message(occasion, recipient, tone, angle):
    # ASK THE AI TO WRITE A PROMPT
    prompt_writer_request = f"""
    You are an expert prompt engineer.
    Write ONE clear prompt that I can give to an AI so it writes a {tone}
    greeting card message for {recipient} on the occasion of {occasion}.

    The prompt should {angle}.
    The prompt must ask for a short message of 3 to 5 sentences.

    Return ONLY the prompt text. Do not write the greeting message itself.
    """
    generated_prompt = ask_gemini(prompt_writer_request).strip()

    # USE THE AI-WRITTEN PROMPT TO GENERATE THE MESSAGE
    message = ask_gemini(generated_prompt)
    return generated_prompt, message


# CREATE THE APPLICATION TITLE AND DESCRIPTION
st.title("💌 AI Greeting Card Assistant")
st.write("Create personalized greeting messages for your loved ones!")

# TAKE INPUT FROM THE USER
occasion = st.text_input("Enter the occasion", placeholder="e.g. Birthday")
recipient = st.text_input("Enter the recipient", placeholder="e.g. My best friend")
tone = st.selectbox("Select the tone", ["Funny", "Formal", "Heartfelt"])

if st.button("Generate Message"):
    # CHECK WHETHER ALL INPUTS ARE PROVIDED
    if occasion.strip() == "" or recipient.strip() == "":
        st.warning("Please enter both occasion and recipient.")
    else:
        with st.spinner("Generating your 3 greeting messages..."):
            try:
                # PROMPT WRITTEN BY ME
                prompt = f"""
                Write a {tone} greeting card message
                for {recipient} on the occasion of {occasion}.

                Keep the message short, warm and creative.
                Write 3 to 5 sentences.
                """
                message_1 = ask_gemini(prompt)

                # PROMPT WRITTEN BY AI
                prompt_2, message_2 = ai_prompt_then_message(occasion, recipient, tone, angle="focus on a personal, emotional touch and warm wording",)

                # 2ND PROMPT WRITTEN BY AI
                prompt_3, message_3 = ai_prompt_then_message(occasion, recipient, tone,angle="focus on creativity, using a playful twist, imagery or a short rhyme",)

                # DISPLAY THE 3 SAMPLES
                st.subheader("Sample 1: Your Greeting Card Message")
                st.caption("Prompt written by me")
                st.markdown(message_1)

                st.subheader("Sample 2: Your Greeting Card Message")
                st.caption("Prompt written by AI[EMOTIONAL TOUCH]")
                with st.expander("See the AI-written prompt"):
                    st.write(prompt_2)
                st.markdown(message_2)

                st.subheader("Sample 3: Your Greeting Card Message")
                st.caption("Prompt written by AI[PLAYFULL TWIST]")
                with st.expander("See the AI-written prompt"):
                    st.write(prompt_3)
                st.markdown(message_3)

            except Exception as e:
                st.error(f"Something went wrong: {e}")