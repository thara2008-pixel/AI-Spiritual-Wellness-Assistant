import plotly.express as px
import pandas as pd
import streamlit as st
import sqlite3

conn = sqlite3.connect(
    "wellness.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Page Settings
st.set_page_config(
    page_title="AI Spiritual Wellness Assistant",
    page_icon="🙏",
    layout="wide"
)

# CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# Title
st.markdown(
    '<h1 class="main-title">🙏 AI Spiritual Wellness Assistant</h1>',
    unsafe_allow_html=True
)

# Navigation
page = st.radio(
    "",
    [
    "🏠 Home",
    "😊 Mood",
    "🧘 Meditation",
    "🌬️ Breathing",
    "📖 Wisdom",
    "🙏 Journal",
    "📊 Dashboard",
    "🤖 AI Coach",
    "🎵 Music",
    "🔐 Login/Register",
    "🏆 Challenges",
    "👤 Profile"
],
    horizontal=True
)

# HOME PAGE
if page == "🏠 Home":

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#ff7b00,#d62828);
    padding:25px;
    border-radius:20px;
    color:white;
    text-align:center;
    ">

    <h1>🙏 Welcome to AI Spiritual Wellness Assistant</h1>

    <p>Balance Mind • Body • Spirit</p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card mood-card">
        <h3>😊 Mood</h3>
        <h2>Good</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card meditation-card">
        <h3>🧘 Meditation</h3>
        <h2>15 Min</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card streak-card">
        <h3>🔥 Streak</h3>
        <h2>7 Days</h2>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card quote-card">
    <h2>🌟 Quote of the Day</h2>
    <p>Peace comes from within. Do not seek it without.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Today's Goal: 10 Min Meditation")

    with col2:
        st.info("🌟 Today's Focus: Inner Peace")

# OTHER PAGES
elif page == "😊 Mood":

    st.title("😊 Mood Analysis")

    mood = st.selectbox(
        "How are you feeling today?",
        [
            "😊 Happy",
            "😌 Calm",
            "😔 Stressed",
            "😟 Anxious",
            "🔥 Motivated",
            "😴 Tired"
        ]
    )

    if st.button("Analyze Mood"):
        cursor.execute(
            "INSERT INTO moods(mood) VALUES(?)",
            (mood,)
        )
        conn.commit()

        if "Happy" in mood:

            st.success("You seem positive and energetic!")

            st.markdown("""
            <div class="ai-card">
            <h3>💡 AI Recommendation</h3>

            ✅ Continue meditation

            ✅ Help someone today

            ✅ Maintain gratitude journal

            </div>
            """, unsafe_allow_html=True)

        elif "Stressed" in mood:

            st.warning("Stress level detected.")

            st.markdown("""
            <div class="card">
            <h3>💡 AI Recommendation</h3>

            ✅ 10-Minute Meditation

            ✅ Deep Breathing

            ✅ Read Daily Wisdom

            </div>
            """, unsafe_allow_html=True)

        elif "Anxious" in mood:

            st.warning("Anxiety detected.")

            st.markdown("""
            <div class="card">
            <h3>💡 AI Recommendation</h3>

            ✅ Focus Meditation

            ✅ Positive Affirmations

            ✅ Relaxation Exercise

            </div>
            """, unsafe_allow_html=True)

        elif "Motivated" in mood:

            st.success("Great energy!")

            st.markdown("""
            <div class="card">
            <h3>💡 AI Recommendation</h3>

            ✅ Set Daily Goals

            ✅ Learn Something New

            ✅ Practice Gratitude

            </div>
            """, unsafe_allow_html=True)

        elif "Calm" in mood:

            st.info("Inner peace detected.")

            st.markdown("""
            <div class="card">
            <h3>💡 AI Recommendation</h3>

            ✅ Continue Meditation

            ✅ Spiritual Reading

            ✅ Mindfulness Practice

            </div>
            """, unsafe_allow_html=True)

        elif "Tired" in mood:

            st.warning("You need rest.")

            st.markdown("""
            <div class="card">
            <h3>💡 AI Recommendation</h3>

            ✅ Sleep Meditation

            ✅ Drink Water

            ✅ Take a Short Break

            </div>
            """, unsafe_allow_html=True)
    st.subheader("📜 Mood History")

    cursor.execute(
        "SELECT mood FROM moods ORDER BY id DESC LIMIT 5"
    )

    history = cursor.fetchall()

    for item in history:
        st.write("•", item[0])

elif page == "🧘 Meditation":

    st.title("🧘 Meditation Center")

    st.write("Choose a meditation session")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
    <div class="stat-card orange">

    <h3>🙏 Journal Entries</h3>

    <h1>{journal_count}</h1>

    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
    <div class="stat-card blue">

    <h3>😊 Mood Records</h3>

    <h1>{mood_count}</h1>

    </div>
    """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">
        <h3>🎯 Focus Meditation</h3>
        <p>15 Minutes</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Start Focus Meditation")

    with col4:

        st.markdown("""
        <div class="card">
        <h3>🌙 Sleep Meditation</h3>
        <p>20 Minutes</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Start Sleep Meditation")

elif page == "📖 Wisdom":

    st.title("📖 Spiritual Wisdom")

    topic = st.selectbox(
        "Choose a Topic",
        [
            "Stress",
            "Success",
            "Discipline",
            "Patience",
            "Focus"
        ]
    )

    if topic == "Stress":

        st.markdown("""
        <div class="card">

        <h2>🕊️ Stress Relief Wisdom</h2>

        <b>Bhagavad Gita</b><br>
        Focus on your actions, not the results.

        </div>
        """, unsafe_allow_html=True)

    elif topic == "Success":

        st.markdown("""
        <div class="card">

        <h2>🏆 Success Wisdom</h2>

        <b>Bhagavad Gita</b><br>
        Success comes through dedicated effort and discipline.

        </div>
        """, unsafe_allow_html=True)

    elif topic == "Discipline":

        st.markdown("""
        <div class="card">

        <h2>🎯 Discipline Wisdom</h2>

        <b>Teaching</b><br>
        Small daily actions create great results.

        </div>
        """, unsafe_allow_html=True)

    elif topic == "Patience":

        st.markdown("""
        <div class="card">

        <h2>🌱 Patience Wisdom</h2>

        <b>Teaching</b><br>
        Growth takes time. Trust the process.

        </div>
        """, unsafe_allow_html=True)

    elif topic == "Focus":

        st.markdown("""
        <div class="card">

        <h2>🧠 Focus Wisdom</h2>

        <b>Teaching</b><br>
        A focused mind can achieve extraordinary things.

        </div>
        """, unsafe_allow_html=True)

elif page == "🙏 Journal":

    st.title("🙏 Gratitude Journal")

    gratitude = st.text_area(
        "What are you grateful for today?"
    )

    if st.button("Save Entry"):

        cursor.execute(
            "INSERT INTO journal(entry) VALUES(?)",
            (gratitude,)
        )

        conn.commit()

        st.success("Entry Saved ✅")

    st.subheader("Previous Entries")

    cursor.execute(
        "SELECT entry FROM journal ORDER BY id DESC"
    )

    data = cursor.fetchall()

    for item in data:

        st.write("•", item[0])

elif page == "📊 Dashboard":

    st.title("📊 Wellness Dashboard")

    # Journal Count
    cursor.execute(
        "SELECT COUNT(*) FROM journal"
    )

    journal_count = cursor.fetchone()[0]

    # Mood Count
    cursor.execute(
        "SELECT COUNT(*) FROM moods"
    )

    mood_count = cursor.fetchone()[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🙏 Journal Entries",
            journal_count
        )

    with col2:
        st.metric(
            "😊 Mood Records",
            mood_count
        )

    st.write("---")

    cursor.execute("""
    SELECT mood, COUNT(*)
    FROM moods
    GROUP BY mood
    """)

    data = cursor.fetchall()

    if data:

        df = pd.DataFrame(
            data,
            columns=["Mood", "Count"]
        )

        fig = px.bar(
            df,
            x="Mood",
            y="Count",
            color="Mood",
            title="Mood Analytics"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.markdown(f"""
<div class="stat-card red">

<h3>🌟 Wellness Score</h3>

<h1>85%</h1>

</div>
""", unsafe_allow_html=True)
elif page == "🌬️ Breathing":

    st.title("🌬️ Breathing Exercises")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
        <h3>🟧 Box Breathing</h3>

        Inhale - 4 sec<br>
        Hold - 4 sec<br>
        Exhale - 4 sec<br>
        Hold - 4 sec

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
        <h3>🔵 Deep Breathing</h3>

        Inhale - 5 sec<br>
        Exhale - 5 sec

        Repeat 10 times

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card">

    <h3>💡 AI Recommendation</h3>

    If you are stressed, practice Box Breathing.

    If you are anxious, practice Deep Breathing.

    </div>
    """, unsafe_allow_html=True)
elif page == "🤖 AI Coach":

    st.title("🤖 AI Wellness Coach")

    user_problem = st.text_area(
        "Tell me what is bothering you..."
    )

    if st.button("Get Advice"):

        if not user_problem:
            st.warning("Please describe your situation.")

        else:

            problem = user_problem.lower()

            if "exam" in problem or "study" in problem:

                st.success("""
                📚 AI Guidance

                ✅ Study in small sessions

                ✅ Take breaks every 45 minutes

                ✅ Focus on progress, not perfection

                ✅ Practice a 5-minute meditation
                """)

            elif "stress" in problem:

                st.success("""
                🌿 Stress Relief Plan

                ✅ Box Breathing

                ✅ 10-Minute Meditation

                ✅ Positive Thinking

                ✅ Read Daily Wisdom
                """)

            elif "sleep" in problem:

                st.success("""
                🌙 Sleep Wellness Tips

                ✅ Reduce screen time

                ✅ Sleep Meditation

                ✅ Consistent sleep schedule
                """)

            else:

                st.success("""
                💡 General Wellness Advice

                ✅ Practice gratitude

                ✅ Stay mindful

                ✅ Take care of your health

                ✅ Keep learning and growing
                """)
elif page == "🎵 Music":

    st.title("🎵 Meditation Music")

    st.write(
        "Relax with calming meditation sounds."
    )

    audio_file = open(
        "assets/meditation.mp3",
        "rb"
    )

    audio_bytes = audio_file.read()

    st.audio(
        audio_bytes,
        format="audio/mp3"
    )

    st.success(
        "Press Play and start relaxing."
    )
elif page == "🔐 Login/Register":

    st.title("🔐 Login & Registration")

    option = st.selectbox(
        "Choose Option",
        ["Register", "Login"]
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if option == "Register":

        if st.button("Register"):

            cursor.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (username, password)
            )

            conn.commit()

            st.success("Registration Successful ✅")

    elif option == "Login":

        if st.button("Login"):

            cursor.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, password)
            )

            user = cursor.fetchone()

            if user:
                st.success("Login Successful ✅")

            else:
                st.error("Invalid Username or Password")
elif page == "🏆 Challenges":

    st.title("🏆 Daily Wellness Challenges")

    challenge1 = st.checkbox(
        "🧘 Meditate for 10 Minutes"
    )

    challenge2 = st.checkbox(
        "🙏 Write a Gratitude Journal Entry"
    )

    challenge3 = st.checkbox(
        "📖 Read Today's Wisdom"
    )

    challenge4 = st.checkbox(
        "🌬️ Complete a Breathing Exercise"
    )

    points = 0

    if challenge1:
        points += 25

    if challenge2:
        points += 25

    if challenge3:
        points += 25

    if challenge4:
        points += 25

    st.metric(
        "⭐ Wellness Points",
        points
    )
    if points == 100:
        st.success(
            "🏅 Level: Wellness Master"
        )

    elif points >= 75:
        st.success(
            "🥇 Level: Advanced"
        )

    elif points >= 50:
        st.info(
            "🥈 Level: Intermediate"
        )

    else:
        st.warning(
            "🥉 Level: Beginner"
        )
elif page == "👤 Profile":

    st.title("👤 User Profile")

    st.markdown("""
    <div class="card">
    
    <h2>Personal Information</h2>

    Name: Thara

    Role: Student

    Project: AI Spiritual Wellness Assistant

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Journal Entries",
            journal_count if 'journal_count' in locals() else 0
        )

    with col2:
        st.metric(
            "Mood Records",
            mood_count if 'mood_count' in locals() else 0
        )

    with col3:
        st.metric(
            "Wellness Level",
            "Advanced"
        )