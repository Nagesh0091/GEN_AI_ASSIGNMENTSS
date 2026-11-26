import streamlit as st
from google import genai

st.set_page_config(page_title="AI Greeting Card Assistant", page_icon="💌", layout="centered")

st.markdown(
    """
    <style>
    .hero {
        background: linear-gradient(135deg, #ff6b9d 0%, #c44fd8 50%, #6a5af9 100%);
        padding: 2rem 1.5rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(196, 79, 216, 0.35);
    }
    .hero h1 { color: white; margin: 0; font-size: 2.2rem; }
    .hero p  { color: rgba(255,255,255,0.92); margin: 0.4rem 0 0 0; font-size: 1.05rem; }

    .card-msg {
        background: linear-gradient(135deg, #fff5f9 0%, #f5f0ff 100%);
        border-left: 6px solid #c44fd8;
        border-radius: 16px;
        padding: 1.4rem 1.6rem;
        font-size: 1.12rem;
        line-height: 1.7;
        color: #2d2540;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        white-space: pre-wrap;
    }
    .badge {
        display: inline-block;
        padding: 0.2rem 0.8rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
        color: white;
    }
    .badge-me { background: #6a5af9; }
    .badge-ai { background: #ff6b9d; }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ff6b9d, #c44fd8, #6a5af9);
        border: none;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 0.7rem 0;
        border-radius: 14px;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) scale(1.01);
        box-shadow: 0 8px 20px rgba(196, 79, 216, 0.45);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("Gemini API key not found. Please add it to secrets.toml.")
    st.stop()

client = genai.Client(api_key=api_key)
MODELS = "gemini-3.5-flash-lite"

OTHER = "✏️ Other (type your own)"

OCCASIONS = {
    "🎂 Birthday": "Birthday",
    "🎉 Anniversary": "Anniversary",
    "💍 Wedding": "Wedding",
    "💞 Engagement": "Engagement",
    "🌹 Valentine's Day": "Valentine's Day",
    "🎓 Graduation": "Graduation",
    "🏆 Congratulations / Achievement": "Congratulations on an achievement",
    "💼 New Job / Promotion": "New Job or Promotion",
    "🏠 Housewarming": "Housewarming",
    "👶 New Baby / Baby Shower": "New Baby or Baby Shower",
    "🪔 Diwali": "Diwali",
    "🎨 Holi": "Holi",
    "🌙 Eid": "Eid",
    "🎄 Christmas": "Christmas",
    "🎆 New Year": "New Year",
    "🪢 Raksha Bandhan": "Raksha Bandhan",
    "🐘 Ganesh Chaturthi": "Ganesh Chaturthi",
    "🕉️ Navratri / Dussehra": "Navratri or Dussehra",
    "🌾 Pongal / Makar Sankranti": "Pongal or Makar Sankranti",
    "🙏 Thank You": "Thank You",
    "🤗 Get Well Soon": "Get Well Soon",
    "🕊️ Condolence / Sympathy": "Condolence and Sympathy",
    "💔 Sorry / Apology": "Apology",
    "🧳 Farewell / Good Luck": "Farewell and Good Luck",
    "👩 Mother's Day": "Mother's Day",
    "👨 Father's Day": "Father's Day",
    "🧑‍🏫 Teacher's Day": "Teacher's Day",
    "🤝 Friendship Day": "Friendship Day",
    "🇮🇳 Independence / Republic Day": "Independence Day or Republic Day",
    "🎁 Just Because": "Just Because, no special occasion",
}

RECIPIENTS = {
    "👫 Best Friend": "My best friend",
    "👩 Mom": "My mom",
    "👨 Dad": "My dad",
    "👭 Sister": "My sister",
    "👬 Brother": "My brother",
    "❤️ Wife": "My wife",
    "💙 Husband": "My husband",
    "💑 Girlfriend": "My girlfriend",
    "💘 Boyfriend": "My boyfriend",
    "👵 Grandmother": "My grandmother",
    "👴 Grandfather": "My grandfather",
    "👧 Daughter": "My daughter",
    "👦 Son": "My son",
    "🧑‍🤝‍🧑 Cousin": "My cousin",
    "👨‍👩‍👧 Uncle / Aunt": "My uncle or aunt",
    "🧑‍🏫 Teacher / Mentor": "My teacher or mentor",
    "💼 Boss": "My boss",
    "🧑‍💻 Colleague / Coworker": "My colleague",
    "👥 Team": "My team",
    "🏡 Neighbour": "My neighbour",
    "🎓 Classmate": "My classmate",
    "👶 Baby / Kid": "A little kid",
    "🧑‍🤝‍🧑 Client / Customer": "A valued client",
}

TONES = {
    "😂 Funny": "Funny",
    "🎩 Formal": "Formal",
    "💖 Heartfelt": "Heartfelt",
    "😍 Romantic": "Romantic",
    "🌟 Inspirational": "Inspirational",
    "😜 Playful": "Playful",
    "😏 Witty / Sarcastic": "Witty and lightly sarcastic",
    "🪶 Poetic": "Poetic",
    "🥹 Emotional": "Emotional",
    "🙇 Respectful": "Respectful",
}

LENGTHS = {
    "Short (2-3 sentences)": "2 to 3 sentences",
    "Medium (3-5 sentences)": "3 to 5 sentences",
    "Long (6-8 sentences)": "6 to 8 sentences",
}

LANGUAGES = ["English", "Hindi", "Marathi", "Hinglish (Hindi + English)", "Gujarati",
             "Tamil", "Telugu", "Bengali", "Urdu", "Spanish", "French", "German"]


def pick(label, options, key, placeholder):
    choice = st.selectbox(label, list(options.keys()) + [OTHER], key=key)
    if choice == OTHER:
        custom = st.text_input(f"Type your own {label.lower()}", placeholder=placeholder, key=key + "_custom")
        return custom.strip()
    return options[choice]


def ask_gemini(prompt):
    response = client.models.generate_content(model=MODELS, contents=prompt)
    return response.text


def ai_prompt_then_message(occasion, recipient, tone, angle, extras):
    prompt_writer_request = f"""
    You are an expert prompt engineer.
    Write ONE clear prompt that I can give to an AI so it writes a {tone}
    greeting card message for {recipient} on the occasion of {occasion}.

    The prompt should {angle}.
    {extras}

    Return ONLY the prompt text. Do not write the greeting message itself.
    """
    generated_prompt = ask_gemini(prompt_writer_request).strip()
    message = ask_gemini(generated_prompt)
    return generated_prompt, message


st.markdown(
    """
    <div class="hero">
        <h1>💌 AI Greeting Card Assistant</h1>
        <p>Create personalized greeting messages for your loved ones!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.subheader("🎯 Tell us about your card")

    col1, col2 = st.columns(2)
    with col1:
        occasion = pick("Occasion", OCCASIONS, "occasion", "e.g. Retirement party")
    with col2:
        recipient = pick("Recipient", RECIPIENTS, "recipient", "e.g. My driving instructor")

    col3, col4 = st.columns(2)
    with col3:
        tone = pick("Tone", TONES, "tone", "e.g. Cheerful and encouraging")
    with col4:
        length_label = st.selectbox("Message length", list(LENGTHS.keys()), index=1)

    with st.expander("✨ More options (optional)"):
        col5, col6 = st.columns(2)
        with col5:
            language = st.selectbox("Language", LANGUAGES)
        with col6:
            sender = st.text_input("Your name (to sign the card)", placeholder="e.g. Rahul")
        details = st.text_area(
            "Anything personal to include?",
            placeholder="e.g. We have been friends since school and love cricket.",
        )

generate = st.button("✨ Generate Message", type="primary", use_container_width=True)

if generate:
    if not occasion or not recipient or not tone:
        st.warning("Please choose (or type) the occasion, recipient and tone.")
    else:
        length = LENGTHS[length_label]

        # OPTIONAL EXTRA LINES ADDED TO THE PROMPTS
        extra_lines = f"Write the message in {language}.\n"
        if sender.strip():
            extra_lines += f"Sign off the message with the name {sender.strip()}.\n"
        if details.strip():
            extra_lines += f"Personal details to include: {details.strip()}\n"

        try:
            with st.status("Creating your greeting cards...", expanded=True) as status:
                # ---------- SAMPLE 1: PROMPT WRITTEN BY ME ----------
                st.write("📝 Writing Sample 1 (my prompt)...")
                prompt_1 = f"""
                Write a {tone} greeting card message
                for {recipient} on the occasion of {occasion}.

                Keep the message short, warm and creative.
                Write {length}.
                {extra_lines}
                """
                message_1 = ask_gemini(prompt_1)

                # ---------- SAMPLE 2: PROMPT WRITTEN BY AI ----------
                st.write("🤖 Writing Sample 2 (AI writes the prompt first)...")
                prompt_2, message_2 = ai_prompt_then_message(
                    occasion, recipient, tone,
                    angle="focus on a personal, emotional touch and warm wording",
                    extras=f"The prompt must ask for a message of {length}.\n{extra_lines}",
                )

                # ---------- SAMPLE 3: PROMPT WRITTEN BY AI ----------
                st.write("🎨 Writing Sample 3 (AI writes the prompt first)...")
                prompt_3, message_3 = ai_prompt_then_message(
                    occasion, recipient, tone,
                    angle="focus on creativity, using a playful twist, imagery or a short rhyme",
                    extras=f"The prompt must ask for a message of {length}.\n{extra_lines}",
                )
                status.update(label="Your cards are ready! 🎉", state="complete", expanded=False)

            st.session_state["results"] = [
                {"title": "Sample 1", "by_ai": False, "prompt": prompt_1.strip(), "message": message_1},
                {"title": "Sample 2", "by_ai": True, "prompt": prompt_2, "message": message_2},
                {"title": "Sample 3", "by_ai": True, "prompt": prompt_3, "message": message_3},
            ]
            st.session_state["heading"] = f"{occasion} · {recipient} · {tone}"
            st.balloons()

        except Exception as e:
            st.error(f"Something went wrong: {e}")

if "results" in st.session_state:
    results = st.session_state["results"]

    st.subheader("💌 Your Greeting Card Messages")
    st.caption(st.session_state["heading"])

    tabs = st.tabs([f"💌 {r['title']}" for r in results])
    for tab, r in zip(tabs, results):
        with tab:
            if r["by_ai"]:
                st.markdown('<span class="badge badge-ai">🤖 Prompt written by AI</span>', unsafe_allow_html=True)
            else:
                st.markdown('<span class="badge badge-me">📝 Prompt written by me</span>', unsafe_allow_html=True)

            # MESSAGE CARD
            safe_text = (
                r["message"].strip()
                .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            )
            st.markdown(f'<div class="card-msg">{safe_text}</div>', unsafe_allow_html=True)

            with st.expander("🔍 See the prompt used"):
                st.write(r["prompt"])

            with st.expander("📋 Copy this message"):
                st.code(r["message"].strip(), language=None)

    # DOWNLOAD ALL SAMPLES
    all_text = "\n\n".join(
        f"=== {r['title']} ({'AI-written prompt' if r['by_ai'] else 'My prompt'}) ===\n{r['message'].strip()}"
        for r in results
    )
    st.download_button(
        "⬇️ Download all messages (.txt)",
        data=all_text,
        file_name="greeting_messages.txt",
        use_container_width=True,
    )

st.markdown("---")
st.caption("Made with ❤️ using Streamlit and Gemini")