import streamlit as st
import base64

st.set_page_config(page_title="Data Science Workshops", layout="wide")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("library_webpage/rutgers_logo.png")

st.markdown(f"""
    <div style="text-align: center; padding-top: 20px;">
        <h1 style="font-size: 48px; font-weight: 800;">Data Science Workshops</h1>
        <p style="font-size: 20px; margin-top: -15px;">
            By <a href="#" style="color: #1E90FF; text-decoration: underline;">Tanya Khanna</a> –
            <span style="color: currentColor;">Data Science Graduate Specialist</span>
        </p>
        <img src="data:image/png;base64,{img_base64}" alt="Rutgers Logo" width="400" style="margin-top: 20px;" />
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .custom-button {
        background-color: #AA4A44;
        color: white;
        padding: 10px 24px;
        font-size: 15px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        animation: fadeIn 1s ease forwards;
        margin: 0px 10px;
        position: relative;
    }

    .custom-button:hover {
        background-color: #922F2A;
    }

    .button-row {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
        margin-bottom: 10px;
    }

    /* Email popup on hover */
    .custom-button[data-email]:hover::after {
        content: attr(data-email);
        position: absolute;
        top: 115%;
        left: 50%;
        transform: translateX(-50%);
        background-color: #ffffff;
        color: #AA4A44;
        padding: 6px 10px;
        border-radius: 6px;
        font-size: 14px;
        font-weight: 500;
        white-space: nowrap;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        animation: fadeIn 0.3s ease forwards;
        z-index: 1000;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="button-row">
        <a href="https://libguides.rutgers.edu/datascience" target="_blank">
            <button class="custom-button">📘 Library Guide</button>
        </a>
        <a href="https://libcal.rutgers.edu/calendar/nblworkshops?cid=4537&t=d&d=0000-00-00&cal=4537&inc=0" target="_blank">
            <button class="custom-button">🗓️ Workshop Calendar</button>
        </a>
        <button class="custom-button" data-email="Email: tanya.khanna@rutgers.edu">📧 Contact Info</button>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

    .typewriter h2 {
      font-family: 'Libre Baskerville', serif;
      font-size: 26px;
      font-weight: 400;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      border-right: 0.15em solid #1E90FF;
      margin: 0 auto;
      width: 46ch;  /* Exact length of sentence + emojis */
      animation: typing 4s steps(46, end), hide-caret 0.5s step-end 4s forwards;
    }

    @keyframes typing {
      from { width: 0 }
      to { width: 46ch }
    }

    @keyframes hide-caret {
      to { border-right: none; }
    }
    </style>

    <div class="typewriter">
        <h2>Pick a topic to get started with your data journey! 🧠 📊</h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

    .slide-in-text {
        font-family: 'Libre Baskerville', serif;
        font-size: 2.2rem;
        font-style: italic;
        color: #236B8E;
        text-align: center;
        margin-top: 30px;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeSlideUp 1.6s ease-out forwards;
    }

    @keyframes fadeSlideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>

    <p class="slide-in-text">Select from the list below to explore available workshops.</p>
""", unsafe_allow_html=True)


selected_topic = st.selectbox(
    "",
    [
        "Python",
        "Data Analysis",
        "Data Science",
        "Advanced Data Science",
        "Generative AI"
    ],
    index=4
)

descriptions = {
    "Python": "Covers beginner to advanced Python workshops, including web scraping and data management using SQL and NoSQL tools.",
    "Data Analysis": "Focuses on data wrangling, visualization, and storytelling using Pandas, NumPy, Matplotlib, and Tableau.",
    "Data Science": "Foundations and techniques in supervised and unsupervised machine learning, plus A/B testing methods.",
    "Advanced Data Science": "Dives deeper into NLP, recommendation systems, ethical AI, and deploying machine learning models.",
    "Generative AI": "Explores large language models, ChatGPT, agent-based AI systems, and the theory and application of GenAI."
}

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');
    .desc-text {{
        font-family: 'Libre Baskerville', serif;
        font-size: 18px;
        color: inherit;
        text-align: center;
        padding-top: 10px;
    }}
    </style>

    <p class="desc-text">{descriptions[selected_topic]}</p>
""", unsafe_allow_html=True)

gif_files = {
    "Python": "library_webpage/python_gif.gif",
    "Data Analysis": "library_webpage/data_analysis_gif.gif",
    "Data Science": "library_webpage/data_science_gif.gif",
    "Advanced Data Science": "library_webpage/advanced_data_science_gif.gif",
    "Generative AI": "library_webpage/generative_ai_gif.gif"
}

gif_path = gif_files[selected_topic]

with open(gif_path, "rb") as f:
    gif_bytes = f.read()
    gif_encoded = base64.b64encode(gif_bytes).decode()

st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/gif;base64,{gif_encoded}" alt="{selected_topic} GIF" width="500"/>
    </div>
""", unsafe_allow_html=True)



if selected_topic == "Generative AI":

    st.markdown("""
        <style>
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .workshop-card-btn {
            background-color: #f2b4b4;
            border-radius: 10px;
            padding: 16px 20px;
            width: 280px;
            min-height: 100px;
            text-align: center;
            font-family: 'Libre Baskerville', serif;
            font-size: 15px;
            color: #1a1a1a;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
            border: none;
            cursor: pointer;
        }
        .workshop-card-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }
        </style>
        <div class="card-grid">
    """, unsafe_allow_html=True)

    workshops = {
        "LLMs Spring 2024": {
            "title": "Large Language Models and ChatGPT (Spring 2024 workshop)",
            "image": "library_webpage/images/llm_spring2024.png",
            "desc": "This workshop gives a clear and easy-to-understand look at cutting-edge language models, especially ChatGPT. Participants will learn how these models are built, trained, and used in real life. The session will also cover how to use them responsibly and follow best practices. By the end, you'll know how large language models work and how to use ChatGPT and similar tools in smart and useful ways.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%209_Large%20Language%20Models/Workshop9-Practical%20Session.ipynb",
            "video": "https://rutgers.app.box.com/s/4xkb3wrodv4ay9mrqou56gfk3d2tlukw",
            "slides": "https://drive.google.com/file/d/1jCWIan-WntBD5rP6f1DwRGbrFpf8Sj-E/view"
        },
        "LLMs Fall 2024": {
            "title": "Large Language Models and ChatGPT (Fall 2024 workshop)",
            "image": "library_webpage/images/llm_fall2024.png",
            "desc": "This workshop gives a clear and easy-to-understand look at cutting-edge language models, especially ChatGPT. Participants will learn how these models are built, trained, and used in real life. The session will also cover how to use them responsibly and follow best practices. By the end, you'll know how large language models work and how to use ChatGPT and similar tools in smart and useful ways.",
            "code": "https://github.com/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/blob/main/Workshop%2011_Large%20Language%20Models%20and%20ChatGPT/app.py",
            "video": "https://rutgers.app.box.com/s/cu4omzc37a04rxyhkyj8hhpg3umds822",
            "slides": "https://drive.google.com/file/d/1CnavzgAXSCdEc7jodyjiBzAXa7ca1CEn/view?usp=sharing"
        },
        "Demystifying GenAI": {
            "title": "Demystifying Generative AI (Spring 2025 workshop)",
            "image": "library_webpage/images/genai_spring2025.png",
            "desc": "This workshop offers a beginner-friendly introduction to generative AI, exploring its capabilities, limitations, and applications in personal and professional contexts. Participants will learn to separate facts from myths, uncover best practices, and discover how to use this transformative technology effectively and ethically.",
            "code": "https://github.com/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/blob/main/Workshop%207/app.py",
            "video": "https://rutgers.app.box.com/s/036kyyakd317riu9affit5x78gnh2xzf",
            "slides": "https://drive.google.com/file/d/1kPxbDeO7XYUMNoG802wPV7Dj3XKpGn7c/view?usp=sharing"
        },
        "LLMs Theory": {
            "title": "Large Language Models: From Theory to Implementation (Spring 2025 workshop)",
            "image": "library_webpage/images/llm_theory_spring2025.png",
            "desc": "This workshop introduces the basics of Large Language Models (LLMs), covering their foundations, capabilities, and practical applications. Learn how to implement LLMs, explore best practices, and responsibly integrate them into real-world projects.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/blob/main/Workshop%208/Workshop8-Practical%20Session.ipynb",
            "video": "https://rutgers.app.box.com/s/j1y82twpj9sb67yphnrihi9c9a3dzep9",
            "slides": "https://drive.google.com/file/d/1MEz801JWMOxuupY6Jwr4scMgQK_2DuHX/view?usp=sharing"
        },
        "AI Agents": {
            "title": "Generative AI Applications with AI Agents (Spring 2025 workshop)",
            "image": "library_webpage/images/ai_agents_spring2025.jpg",
            "desc": "This workshop explores the integration of generative AI with autonomous agents to create innovative applications that can solve problems, automate tasks, and enhance creativity. Participants will learn how generative AI agents combine language models, tools, and APIs to perform complex tasks independently.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/blob/main/Workshop%209/research_assistant_with_AI_agents.ipynb",
            "video": "https://rutgers.app.box.com/s/ljvlwwa09u9cjvkp5uee1co377i7s4j7",
            "slides": "https://drive.google.com/file/d/1uoVP8aB4rhmR6pVedFLyZy9TBRiMKBIE/view?usp=sharing"
        }
    }


    for key, info in workshops.items():
        if st.button(info["title"], key=key, use_container_width=True):
            st.session_state["selected_generative_ai_workshop"] = key

    st.markdown("</div>", unsafe_allow_html=True)
    
    if "selected_generative_ai_workshop" in st.session_state:
        selected_key = st.session_state["selected_generative_ai_workshop"]
        if selected_key in workshops:
            wk = workshops[selected_key]

        
        st.markdown(f"""
            <h3 style='text-align: center; font-family: "Libre Baskerville", serif;'>🎓 {wk['title']}</h3>
        """, unsafe_allow_html=True)

        
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src="data:image/gif;base64,{base64.b64encode(open(wk['image'], "rb").read()).decode()}" width="800">
            </div>
        """, unsafe_allow_html=True)

        
        st.markdown(f"""
            <p style='text-align: center; font-family: "Libre Baskerville", serif; font-size: 16px; margin-top: 20px;'>
                {wk['desc']}
            </p>
        """, unsafe_allow_html=True)

        st.markdown("""
                <style>
                .button-row {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin-top: 30px;
                    flex-wrap: wrap;
                }

                .resource-button {
                    background-color: #dddddd;  /* Light gray: readable on both themes */
                    color: #1a1a1a;             /* Dark text */
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-size: 15px;
                    font-family: "Libre Baskerville", serif;
                    text-decoration: none !important;  /* <- THIS REMOVES underline */
                    transition: background-color 0.3s ease;
                    display: inline-block;
                }

                .resource-button:hover {
                    background-color: #bbbbbb; /* Slightly darker on hover */
                }
                </style>""", unsafe_allow_html=True)

        
        st.markdown(f"""
            <div class="button-row">
                <a href="{wk['code']}" target="_blank" class="resource-button">💻 Code</a>
                <a href="{wk['video']}" target="_blank" class="resource-button">📽️ Video</a>
                <a href="{wk['slides']}" target="_blank" class="resource-button">📁 Slides</a>
            </div>
        """, unsafe_allow_html=True)



if selected_topic == "Advanced Data Science":

    st.markdown("""
        <style>
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .workshop-card-btn {
            background-color: #f2b4b4;
            border-radius: 10px;
            padding: 16px 20px;
            width: 280px;
            min-height: 100px;
            text-align: center;
            font-family: 'Libre Baskerville', serif;
            font-size: 15px;
            color: #1a1a1a;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
            border: none;
            cursor: pointer;
        }
        .workshop-card-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }
        </style>
        <div class="card-grid">
    """, unsafe_allow_html=True)

    workshops = {
        "DL Spring 2024": {
            "title": "Introduction to Deep Learning (Spring 2024 workshop)",
            "image": "library_webpage/images/1-d89926d0.png",
            "desc": "This workshop offers an introduction to the fundamentals of deep learning, a highly influential branch of artificial intelligence. This session focuses on the core concepts of neural networks, including feedforward neural networks, the simplest type of artificial neural network architecture. The course also covers convolutional neural networks (CNNs), essential for image and video recognition, and recurrent neural networks (RNNs), which are crucial for handling sequential data like text and speech.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop_7_Deep_Learning/Recurrent_Neural_Networks.ipynb",
            "video": "https://rutgers.app.box.com/s/u45bm5qo692rxl5yf3znvkei8qxcihi7",
            "slides": "https://drive.google.com/file/d/14p9947uh1Mpv-YaeRpgm1Xy30LZN9hoU/view"
        },
        "NLP Spring 2024": {
            "title": "Deep Dive into Natural Language Processing (Spring 2024 workshop)",
            "image": "library_webpage/images/ChatGPT Image Apr 22, 2025, 12_32_48 PM.png",
            "desc": "Are you eager to learn how to communicate with computer systems using Natural Language Processing (NLP) techniques, or to make machines understand human sentiments? Do you aspire to build intelligent applications like Siri, Alexa, or chatbots, even if you're starting from scratch? This workshop introduces Natural Language Processing (NLP), teaching you to preprocess text, analyze sentiments, model topics, and use language generation models. It's perfect for anyone eager to build applications that interact naturally with human language.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%208_Natural%20Language%20Processing/Deep-Dive-into-Natural-Language-Processing.ipynb",
            "video": "https://rutgers.app.box.com/s/zxnowedjxpv7hr66joiqvlrvlcrdobk0",
            "slides": "https://drive.google.com/file/d/1y2fDEczq8MzqDFdhVpBpIWMYzJzQy3dy/view"
        },
        "Ethical AI": {
            "title": "Ethical AI and Responsible Data Science (Fall 2024 workshop)",
            "image": "library_webpage/images/e99ce085-b7c4-4a4b-9c8f-50bea243efed.png",
            "desc": "This workshop will explore the ethical considerations in AI and data science, focusing on designing and implementing fair, transparent, and accountable systems.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/blob/main/Workshop%2010_EthicalAI_and_Responsible%20Data%20Science/XAI%20and%20Bias-Detection.ipynb",
            "video": "https://rutgers.app.box.com/s/j0nde4plp0o1bq0o5ywxbef9915rj8nd",
            "slides": "https://drive.google.com/file/d/1i8CwKIHv6rcT7UOjvXXexgYTt27qb2n5/view?usp=sharing"
        },
        "Deploying ML": {
            "title": "Deploying Machine Learning Models (Fall 2024 workshop)",
            "image": "library_webpage/images/33d4a7e1-4043-4eaa-9415-70b265158981.png",
            "desc": "This workshops will equip participants with the knowledge and skills necessary to transition machine learning models from development to production, focusing on modern deployment technologies and practices.",
            "code": "https://github.com/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/tree/main/Workshop_9_Deploying_Machine_Learning_Models",
            "video": "https://rutgers.app.box.com/s/l41e5fcojc0mzlgwoo177m8j5b86g6m1",
            "slides": "https://drive.google.com/file/d/1oBtCRO-8P-GSI4mX4wSuVqlid0_LHZq1/view?usp=sharing"
        },
        "RecSys": {
            "title": "Building Intelligent Recommendation Systems (Spring 2025 workshop)",
            "image": "library_webpage/images/0_0GclG1YS4i6O2mKV.png",
            "desc": "Dive into the fascinating world of recommender systems, the backbone of personalized experiences in today’s digital age. In this workshop, you’ll uncover how platforms like Netflix, Amazon, and Spotify predict what users want. Participants will gain insights into popular algorithms, including collaborative and content-based filtering, and apply these techniques to create intelligent recommendation solutions.",
            "code": "https://github.com/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/tree/main/Workshop%2010/cine-mate",
            "video": "https://rutgers.app.box.com/s/lgy3qxn3o1x52ep99ht3jajedh5qn1rw",
            "slides": "https://drive.google.com/file/d/15aY1M9EzLIwMrOH4aW3rbzqVI9m0Mg65/view?usp=sharing"
        }
    }

  
    for key, info in workshops.items():
        if st.button(info["title"], key=key, use_container_width=True):
            st.session_state["selected_advanced_data_science_workshop"] = key

    st.markdown("</div>", unsafe_allow_html=True)

    
    if "selected_advanced_data_science_workshop" in st.session_state:
        selected_key = st.session_state["selected_advanced_data_science_workshop"]
        if selected_key in workshops:
            wk = workshops[selected_key]

       
        st.markdown(f"""
            <h3 style='text-align: center; font-family: "Libre Baskerville", serif;'>🎓 {wk['title']}</h3>
        """, unsafe_allow_html=True)


        st.markdown(f"""
            <div style='text-align: center;'>
                <img src="data:image/gif;base64,{base64.b64encode(open(wk['image'], "rb").read()).decode()}" width="800">
            </div>
        """, unsafe_allow_html=True)


        st.markdown(f"""
            <p style='text-align: center; font-family: "Libre Baskerville", serif; font-size: 16px; margin-top: 20px;'>
                {wk['desc']}
            </p>
        """, unsafe_allow_html=True)

        st.markdown("""
                <style>
                .button-row {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin-top: 30px;
                    flex-wrap: wrap;
                }

                .resource-button {
                    background-color: #dddddd;  /* Light gray: readable on both themes */
                    color: #1a1a1a;             /* Dark text */
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-size: 15px;
                    font-family: "Libre Baskerville", serif;
                    text-decoration: none !important;  /* <- THIS REMOVES underline */
                    transition: background-color 0.3s ease;
                    display: inline-block;
                }

                .resource-button:hover {
                    background-color: #bbbbbb; /* Slightly darker on hover */
                }
                </style>""", unsafe_allow_html=True)

     
        st.markdown(f"""
            <div class="button-row">
                <a href="{wk['code']}" target="_blank" class="resource-button">💻 Code</a>
                <a href="{wk['video']}" target="_blank" class="resource-button">📽️ Video</a>
                <a href="{wk['slides']}" target="_blank" class="resource-button">📁 Slides</a>
            </div>
        """, unsafe_allow_html=True)


if selected_topic == "Data Analysis":

    st.markdown("""
        <style>
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .workshop-card-btn {
            background-color: #f2b4b4;
            border-radius: 10px;
            padding: 16px 20px;
            width: 280px;
            min-height: 100px;
            text-align: center;
            font-family: 'Libre Baskerville', serif;
            font-size: 15px;
            color: #1a1a1a;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
            border: none;
            cursor: pointer;
        }
        .workshop-card-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }
        </style>
        <div class="card-grid">
    """, unsafe_allow_html=True)

    workshops = {
        "MDA_S24": {
            "title": "Mastering Data Analysis: Pandas and NumPy Essentials (Spring 2024 workshop)",
            "image": "library_webpage/images/82f29cbd-b150-4a62-a7ac-064327f8cb79.png",
            "desc": "This workshop is designed to equip learners with powerful tools for data analysis in Python. Participants will delve into the world of NumPy, exploring its efficient arrays and array operations, which form the backbone of numerical computing in Python. The workshop then shifts to Pandas, where learners will get hands-on experience with its fundamental data structures - Series and DataFrame. This comprehensive session is ideal for anyone looking to enhance their data analysis skills, offering the tools needed to unlock insights from data with efficiency and precision.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop_2_Numpy_Pandas/Mastering%20Data%20Analysis%20-%20Pandas%20and%20NumPy%20Essentials.ipynb",
            "video": "https://rutgers.app.box.com/s/86tttuh40jv5y91v2wc5x20nw8wd3cd8",
            "slides": "https://drive.google.com/file/d/1hGmqXrAVJzqMKG1vaRWq1mTZaFMzJBzc/view"
        },
        "MDA_F24": {
            "title": "Mastering Data Analysis: Pandas and NumPy Essentials (Fall 2024 workshop)",
            "image": "library_webpage/images/82f29cbd-b150-4a62-a7ac-064327f8cb79.png",
            "desc": "This workshop is designed to equip learners with powerful tools for data analysis in Python. Participants will delve into the world of NumPy, exploring its efficient arrays and array operations, which form the backbone of numerical computing in Python. The workshop then shifts to Pandas, where learners will get hands-on experience with its fundamental data structures - Series andDataFrame. This comprehensive session is ideal for anyone looking to enhance their data analysis skills, offering the tools needed to unlock insights from data with efficiency and precision.",
            "code": "https://github.com/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/tree/main/Workshop_4_Numpy_Pandas",
            "video": "https://rutgers.app.box.com/s/9qbsk5dm8t0q8xptls2q2rx0938g40y4",
            "slides": "https://drive.google.com/file/d/1JMLCuTsHWYo7uXjWzQmZKKZk5G-PzndT/view?usp=sharing"
        },
        "MDA_S25": {
            "title": "Mastering Data Analysis: Pandas and NumPy Essentials (Spring 2025 workshop)",
            "image": "library_webpage/images/82f29cbd-b150-4a62-a7ac-064327f8cb79.png",
            "desc": "This workshop is designed to equip learners with powerful tools for data analysis in Python. Participants will delve into the world of NumPy, exploring its efficient arrays and array operations, which form the backbone of numerical computing in Python. The workshop then shifts to Pandas, where learners will get hands-on experience with its fundamental data structures - Series and DataFrame. This comprehensive session is ideal for anyone looking to enhance their data analysis skills, offering the tools needed to unlock insights from data with efficiency and precision.",
            "code": "https://github.com/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/tree/main/Workshop%202",
            "video": "https://rutgers.app.box.com/s/hx825x2uvp1ktrodfpvskr2jpw9jvrch",
            "slides": "https://drive.google.com/file/d/1IAxG2OVzm2Wb4vZynElfsdo-y9Z2LBy3/view?usp=sharing"
        },
        "Visualization": {
            "title": "Unveiling Data Stories: Python for Visualization and Exploration (Spring 2024 workshop)",
            "image": "library_webpage/images/workshop3_resized (1).png",
            "desc": "This workshop is designed to guide participants through the process of revealing hidden stories in data using Python. It focuses on using Matplotlib and Seaborn, two prominent visualization tools, for effective exploratory data analysis (EDA). This workshop emphasizes the creation of engaging visual narratives, enabling participants to transform complex data insights into compelling and understandable visual formats.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop_3_Data%20Viz%20&%20Exploration/Python%20for%20Visualization%20and%20Exploration.ipynb",
            "video": "https://rutgers.app.box.com/s/f7w64jvm9txqhj3wrg0byne73qsx9dnl",
            "slides": "https://drive.google.com/file/d/1YDNQlAV9XDnPW-wdJh2-ElFKjR-M8xRh/view"
        },
        "Exploration": {
            "title": "Python for Visualization and Exploration (Fall 2024 workshop)",
            "image": "library_webpage/images/1-b02ffaff.jpg",
            "desc": "This workshop is designed to guide participants through the process of revealing hidden stories in data using Python. It focuses on using Matplotlib, for effective exploratory data analysis (EDA). This workshop emphasizes the creation of engaging visual narratives, enabling participants to transform complex data insights into compelling and understandable visual formats. Interactive visualizations using libraries like Plotly, which allow for dynamic, browser-based graphs. Also, crafting narratives and storytelling with data - best practices for presenting data insights.",
            "code": "https://github.com/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/tree/main/Workshop6_Python%20for%20Visualization%20and%20Exploration",
            "video": "https://rutgers.app.box.com/s/j9iwtb3mszi1yqai5baqadiiq8x2jp4g",
            "slides": "https://drive.google.com/file/d/1sukqRQ_ss4DIay3NcJU4xRjr-EGVdfqI/view?usp=sharing"
        },
        "Tableau": {
            "title": "Introduction to Tableau: Visualizing Data Made Easy (Spring 2025 workshop)",
            "image": "library_webpage/images/create-complex-elegant-and-robust-dashboards-and-solutions.png",
            "desc": "This workshop provides a concise introduction to Tableau, a powerful tool for creating interactive data visualizations. Participants will learn how to create interactive dashboards, visualize complex datasets, and uncover insights through dynamic charts and graphs. This hands-on session will guide you through the essentials of Tableau, including data connection, transformation, and storytelling techniques.",
            "code": "https://github.com/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/tree/main/Workshop%203",
            "video": "https://rutgers.app.box.com/s/8qfa3961j2y1fivy0ktzzirz2fn6pyq9",
            "slides": "https://drive.google.com/file/d/1W87ksom0Ok5yV9d2JpJT2SL4cAnaoONO/view?usp=sharing"
        }
    }


    for key, info in workshops.items():
        if st.button(info["title"], key=key, use_container_width=True):
            st.session_state["selected_data_analysis_workshop"] = key

    st.markdown("</div>", unsafe_allow_html=True)


    if "selected_data_analysis_workshop" in st.session_state:
        selected_key = st.session_state["selected_data_analysis_workshop"]
        if selected_key in workshops:
            wk = workshops[selected_key]


        st.markdown(f"""
            <h3 style='text-align: center; font-family: "Libre Baskerville", serif;'>🎓 {wk['title']}</h3>
        """, unsafe_allow_html=True)


        st.markdown(f"""
            <div style='text-align: center;'>
                <img src="data:image/gif;base64,{base64.b64encode(open(wk['image'], "rb").read()).decode()}" width="800">
            </div>
        """, unsafe_allow_html=True)


        st.markdown(f"""
            <p style='text-align: center; font-family: "Libre Baskerville", serif; font-size: 16px; margin-top: 20px;'>
                {wk['desc']}
            </p>
        """, unsafe_allow_html=True)

        st.markdown("""
                <style>
                .button-row {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin-top: 30px;
                    flex-wrap: wrap;
                }

                .resource-button {
                    background-color: #dddddd;  /* Light gray: readable on both themes */
                    color: #1a1a1a;             /* Dark text */
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-size: 15px;
                    font-family: "Libre Baskerville", serif;
                    text-decoration: none !important;  /* <- THIS REMOVES underline */
                    transition: background-color 0.3s ease;
                    display: inline-block;
                }

                .resource-button:hover {
                    background-color: #bbbbbb; /* Slightly darker on hover */
                }
                </style>""", unsafe_allow_html=True)

      
        st.markdown(f"""
            <div class="button-row">
                <a href="{wk['code']}" target="_blank" class="resource-button">💻 Code</a>
                <a href="{wk['video']}" target="_blank" class="resource-button">📽️ Video</a>
                <a href="{wk['slides']}" target="_blank" class="resource-button">📁 Slides</a>
            </div>
        """, unsafe_allow_html=True)


if selected_topic == "Python":

    st.markdown("""
        <style>
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .workshop-card-btn {
            background-color: #f2b4b4;
            border-radius: 10px;
            padding: 16px 20px;
            width: 280px;
            min-height: 100px;
            text-align: center;
            font-family: 'Libre Baskerville', serif;
            font-size: 15px;
            color: #1a1a1a;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
            border: none;
            cursor: pointer;
        }
        .workshop-card-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }
        </style>
        <div class="card-grid">
    """, unsafe_allow_html=True)


    workshops = {
        "PythonS24": {
            "title": "Introduction to Python Programming (Spring 2024 workshop)",
            "image": "library_webpage/images/python 1.png",
            "desc": "This workshop is designed for beginners with little to no experience in programming, aiming to provide a rapid yet comprehensive introduction to the world of Python, one of the most popular and versatile programming languages today. Learners will quickly grasp Python syntax, script execution, and fundamental constructs like variables, data types, and operators. They will also explore control structures like if-else statements, loops, and functions, gaining practical skills in data structures such as lists, tuples, sets, and dictionaries. Additionally, the workshop covers file handling and text processing.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%201_Introduction%20to%20Python/1.%20Introduction%20to%20Python%20Programming.ipynb",
            "video": "https://rutgers.app.box.com/s/28oms37i6vyb77d042zssxwy9dehodvr",
            "slides": "https://drive.google.com/file/d/19prKM96ZKK0m0YiD2xAEUhjhsf2VGF72/view"
        },
        "PythonF24": {
            "title": "Introduction to Python Programming (Fall 2024 workshop)",
            "image": "library_webpage/images/python 1.png",
            "desc": "This workshop is designed for beginners with little to no experience in programming, aiming to provide a rapid yet comprehensive introduction to the world of Python, one of the most popular and versatile programming languages today. Introduction to Jupyter Notebook and Google Collab. Learners will quickly grasp Python syntax, script execution, and fundamental constructs like variables, data types, and operators. They will also explore control structures like if-else statements, loops, and functions, gaining practical skills in data structures such as lists, tuples, sets, and dictionaries.",
            "code": "https://github.com/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/tree/main/Workshop1_Introduction_to_Python",
            "video": "https://rutgers.app.box.com/s/fhc00rumvlp59aeqos7ir1ry4yiub0nr",
            "slides": "https://drive.google.com/file/d/1w_5thc7z0k6FrTmX8Dt2HMgOnEG2ExSP/view?usp=sharing"
        },
        "PythonS25": {
            "title": "Introduction to Python Programming (Spring 2025 workshop)",
            "image": "library_webpage/images/python 1.png",
            "desc": "This workshop is designed for beginners with little to no experience in programming, aiming to provide a rapid yet comprehensive introduction to the world of Python, one of the most popular and versatile programming languages today. Introduction to Jupyter Notebook and Google Collab. Learners will quickly grasp Python syntax, script execution, and fundamental constructs like variables, data types, and operators. They will also explore control structures like if-else statements, loops, and functions, gaining practical skills in data structures such as lists, tuples, sets, and dictionaries.",
            "code": "https://github.com/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/tree/main/Workshop%201",
            "video": "https://rutgers.app.box.com/s/8h08witt5xhp9fowg31vfivnc55gxgz6",
            "slides": "https://drive.google.com/file/d/1xYzI0m56GEwPDSSb-sdq1kniZ6kC9jsW/view?usp=sharing"
        },
        "AdvancedPython": {
            "title": "Advanced Python Programming (Fall 2024 workshop)",
            "image": "library_webpage/images/1632087530299.png",
            "desc": "The workshop covers debugging and error handling in Python to help participants understand common programming errors and how to fix them. Object-oriented Programming. Functional Programming in Python: Concepts of functional programming: immutability, first-class functions, and pure functions. Using lambda, map, filter, reduce for functional style programming. One-two data structures.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/blob/main/Workshop2_Advanced_Python/Workshop2-Advanced%20Python%20Programming.ipynb",
            "video": "https://rutgers.app.box.com/s/f39hp5sznrile3d8cewm1ipzxsoho7ed",
            "slides": "https://drive.google.com/file/d/19ZjxqF8S1IO0URLl1kJ2mZouG6UVKVEC/view?usp=sharing"
        },
        "WebScraping": {
            "title": "Web Scraping with Python: Techniques and Ethics (Fall 2024 workshop)",
            "image": "library_webpage/images/python 2.png",
            "desc": "This workshop will teach participants how to programmatically gather data from the internet using Python, focusing on legal and ethical considerations.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/blob/main/Workshop3_Web_Scraping_with_Python/Web%20Scraping%20with%20Python.ipynb",
            "video": "https://rutgers.app.box.com/s/b4ra16r5d8cmn8pjjwqpu004gnliq0x2",
            "slides": "https://drive.google.com/file/d/1h-sOFjN-EjoC6N4l86bxgFlZ0z9hJSqv/view?usp=sharing"
        },
        "SQLPython": {
            "title": "Data Management with Python Workshop (SQL and NoSQL) (Fall 2024 workshop)",
            "image": "library_webpage/images/Screenshot 2025-04-24 at 7.29.03 PM.png",
            "desc": "Equip participants with the skills to effectively interact with both SQL and NoSQL databases using Python, highlighting the appropriate use cases and best practices for each.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/blob/main/Workshop_5_Data_Management_Python/Data%20Management%20with%20Python.ipynb",
            "video": "https://rutgers.app.box.com/s/ndtwyz7hw2fg7v1k9ephw62omezykka5",
            "slides": "https://drive.google.com/file/d/1poGH5-3wf3XOSFHaFXiKJZ6sG_8_x6Pq/view?usp=sharing"
        }
    }


    for key, info in workshops.items():
        if st.button(info["title"], key=key, use_container_width=True):
            st.session_state["selected_python_workshop"] = key

    st.markdown("</div>", unsafe_allow_html=True)


    if "selected_python_workshop" in st.session_state:
        selected_key = st.session_state["selected_python_workshop"]
        if selected_key in workshops:
            wk = workshops[selected_key]


        st.markdown(f"""
            <h3 style='text-align: center; font-family: "Libre Baskerville", serif;'>🎓 {wk['title']}</h3>
        """, unsafe_allow_html=True)

      
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src="data:image/gif;base64,{base64.b64encode(open(wk['image'], "rb").read()).decode()}" width="800">
            </div>
        """, unsafe_allow_html=True)


        st.markdown(f"""
            <p style='text-align: center; font-family: "Libre Baskerville", serif; font-size: 16px; margin-top: 20px;'>
                {wk['desc']}
            </p>
        """, unsafe_allow_html=True)

        st.markdown("""
                <style>
                .button-row {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin-top: 30px;
                    flex-wrap: wrap;
                }

                .resource-button {
                    background-color: #dddddd;  /* Light gray: readable on both themes */
                    color: #1a1a1a;             /* Dark text */
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-size: 15px;
                    font-family: "Libre Baskerville", serif;
                    text-decoration: none !important;  /* <- THIS REMOVES underline */
                    transition: background-color 0.3s ease;
                    display: inline-block;
                }

                .resource-button:hover {
                    background-color: #bbbbbb; /* Slightly darker on hover */
                }
                </style>""", unsafe_allow_html=True)

       
        st.markdown(f"""
            <div class="button-row">
                <a href="{wk['code']}" target="_blank" class="resource-button">💻 Code</a>
                <a href="{wk['video']}" target="_blank" class="resource-button">📽️ Video</a>
                <a href="{wk['slides']}" target="_blank" class="resource-button">📁 Slides</a>
            </div>
        """, unsafe_allow_html=True)


if selected_topic == "Data Science":

    st.markdown("""
        <style>
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .workshop-card-btn {
            background-color: #f2b4b4;
            border-radius: 10px;
            padding: 16px 20px;
            width: 280px;
            min-height: 100px;
            text-align: center;
            font-family: 'Libre Baskerville', serif;
            font-size: 15px;
            color: #1a1a1a;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
            border: none;
            cursor: pointer;
        }
        .workshop-card-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }
        </style>
        <div class="card-grid">
    """, unsafe_allow_html=True)

    workshops = {
        "MathFoundation": {
            "title": "Mathematical Foundations for Data Science (Spring 2024 workshop)",
            "image": "library_webpage/images/prediction.png",
            "desc": "This workshop offers a brief yet comprehensive overview of essential mathematics for data science. It covers foundational statistics and probability, crucial for model understanding, and basic hypothesis testing techniques. It also introduces linear algebra concepts like vectors and matrices, alongside fundamental calculus for derivatives and integrals.",
            "code": None,
            "video": "https://rutgers.app.box.com/s/6vfncnhgng6mmb6e4mci1m76djzo8sy0",
            "slides": "https://drive.google.com/file/d/103VXTSYxd64egPD7isStTdO9XzWNb6Bq/view"
        },
        "MLS_S24": {
            "title": "Introduction to Machine Learning: Supervised Learning (Spring 2024 workshop)",
            "image": "library_webpage/images/regression-vs.png",
            "desc": "This workshop is tailored for beginners in machine learning. It focuses on supervised learning algorithms that are a cornerstone of machine learning, where the algorithm learns from labeled training data, helping to predict outcomes for unforeseen data. Classification and Regression will be introduced. Participants will learn about key algorithms like Linear Regression and Decision Trees, exploring how these methods enable machines to learn from and make predictions based on data.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%205_Machine%20Learning-Supervised/ML%20-%20Supervised%20Learning.ipynb",
            "video": "https://rutgers.app.box.com/s/vvjmyzdo6ndgqu5hkh8bol9s1gya6re9",
            "slides": "https://drive.google.com/file/d/1Jfw_JCRvalteKgf8OZJLpWFjczRreTGx/view?usp=sharing"
        },
        "MLS_F24": {
            "title": "Introduction to Machine Learning: Supervised Learning (Fall 2024 workshop)",
            "image": "library_webpage/images/regression-vs.png",
            "desc": "This workshop is tailored for beginners in machine learning. It focuses on supervised learning algorithms that are a cornerstone of machine learning, where the algorithm learns from labeled training data, helping to predict outcomes for unforeseen data. Classification and Regression will be introduced. Participants will learn about key algorithms like Linear Regression and ensemble methods like Random Forests and Gradient Boosting Machines for improved prediction accuracy.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/blob/main/Workshop%207_Machine%20Learning-Supervised/ML%20-%20Supervised%20Learning.ipynb",
            "video": "https://rutgers.app.box.com/s/04kdfex3k7puwz97no0rbygopwcrx1gw",
            "slides": "https://drive.google.com/file/d/1fVXSLS3c4lVr6BAEODbEc2nO6dpYj3_I/view?usp=sharing"
        },
        "MLS_S25": {
            "title": "Introduction to Machine Learning: Supervised Learning (Spring 2025 workshop)",
            "image": "library_webpage/images/regression-vs.png",
            "desc": "This workshop is tailored for beginners in machine learning. It focuses on supervised learning algorithms that are a cornerstone of machine learning, where the algorithm learns from labeled training data, helping to predict outcomes for unforeseen data. Classification and Regression will be introduced. Participants will learn about key algorithms like Linear Regression and ensemble methods like Random Forests and Gradient Boosting Machines for improved prediction accuracy.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/blob/main/Workshop%204/ML%20-%20Supervised%20Learning.ipynb",
            "video": "https://rutgers.app.box.com/s/uqp5e7xoj3846fk7wfp27ryubic3e5rp",
            "slides": "https://drive.google.com/file/d/1Vnjl9O4MFgG2cDFbYPUP671l0s6hXEZP/view?usp=sharing"
        },
        "MLUS_S24": {
            "title": "Introduction to Machine Learning: Unsupervised Learning (Spring 2024 workshop)",
            "image": "library_webpage/images/1786ca0eI0HsoLG_j9AqVfA.gif",
            "desc": "This workshop is designed to introduce the concepts of unsupervised learning, a branch of machine learning where algorithms infer patterns from unlabelled data. The course covers clustering methods like K-means and DBSCAN, used to identify inherent groupings in data. It also explores dimensionality reduction techniques such as PCA, which simplify complex data sets while preserving their key features. Additionally, the session introduces association rules, a method for finding interesting relationships within data sets. This workshop is ideal for those interested in learning how to extract insights from data without predetermined labels or categories.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%206_Machine%20Learning-Unsupervised/Machine%20Learning%20-%20Unsupervised%20Learning.ipynb",
            "video": "https://rutgers.app.box.com/s/c3ah73jfqc72mrrl3nezl9wszxptu5fu",
            "slides": "https://drive.google.com/file/d/1q9QLi70r34aTWDsrmK4VITdNzdNQ3zV4/view?usp=sharing"
        },
        "MLUS_F24": {
            "title": "Introduction to Machine Learning: Unsupervised Learning (Fall 2024 workshop)",
            "image": "library_webpage/images/1786ca0eI0HsoLG_j9AqVfA.gif",
            "desc": "This workshop is designed to introduce the concepts of unsupervised learning, a branch of machine learning where algorithms infer patterns from unlabelled data. The course covers clustering methods like K-means and DBSCAN, used to identify inherent groupings in data. It also explores dimensionality reduction techniques such as PCA, which simplify complex data sets while preserving their key features. Additionally, the session introduces association rules, a method for finding interesting relationships within data sets. This workshop is ideal for those interested in learning how to extract insights from data without predetermined labels or categories.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/DataScienceWorkshop_Fall-2024_NBL/blob/main/Workshop%208_Machine%20Learning-Unsupervised/Machine%20Learning%20-%20Unsupervised%20Learning.ipynb",
            "video": "https://rutgers.app.box.com/s/z6wxmw3cawut9m3hylx70e6hhlj5xwic",
            "slides": "https://drive.google.com/file/d/1MaQ0CrhfgY_QXla7WeqEfRZTo99ea6vz/view?usp=sharing"
        },
        "MLUS_S25": {
            "title": "Introduction to Machine Learning: Unsupervised Learning (Spring 2025 workshop)",
            "image": "library_webpage/images/1786ca0eI0HsoLG_j9AqVfA.gif",
            "desc": "This workshop is designed to introduce the concepts of unsupervised learning, a branch of machine learning where algorithms infer patterns from unlabelled data. The course covers clustering methods like K-means and DBSCAN, used to identify inherent groupings in data. It also explores dimensionality reduction techniques such as PCA, which simplify complex data sets while preserving their key features. Additionally, the session introduces association rules, a method for finding interesting relationships within data sets. This workshop is ideal for those interested in learning how to extract insights from data without predetermined labels or categories.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/blob/main/Workshop%205/Machine%20Learning%20-%20Unsupervised%20Learning.ipynb",
            "video": "https://rutgers.app.box.com/s/gx23d0ay5v5aie3e7y2qgqw95ud6976z",
            "slides": "https://drive.google.com/file/d/1ixDto3dXvLVVStDKMX3amGWa9FU19U36/view?usp=sharing"
        },
        "HypothesisTesting": {
            "title": "Data-Driven Decision Making: A/B Testing and Statistical Hypothesis Testing (Spring 2025 workshop)",
            "image": "library_webpage/images/1_VhPfZIYkcnV-vWZYaAvgjg.jpg",
            "desc": "This workshop aims to equip participants with the knowledge and skills to implement A/B testing and statistical hypothesis testing for data-driven decision-making. The session will cover fundamental concepts, practical implementation, and interpretation of results, enabling attendees to make informed decisions based on empirical data.",
            "code": "https://nbviewer.org/github/Tanya-Khanna/Data-Science-Workshop---Spring-2025---NBL-/blob/main/Workshop%206/Hypothesis%20Testing.ipynb",
            "video": "https://rutgers.app.box.com/s/f849m04zfmnw09ogibhral08f6phkhbh",
            "slides": "https://drive.google.com/file/d/1PrG8GAKswoVrjKjWAW-N27Y4B0R14jNP/view?usp=sharing"
        }
    }

    for key, info in workshops.items():
        if st.button(info["title"], key=key, use_container_width=True):
            st.session_state["selected_data_science_workshop"] = key

    st.markdown("</div>", unsafe_allow_html=True)

    if "selected_data_science_workshop" in st.session_state:
        selected_key = st.session_state["selected_data_science_workshop"]
        if selected_key in workshops:
            wk = workshops[selected_key]

        st.markdown(f"""
            <h3 style='text-align: center; font-family: "Libre Baskerville", serif;'>🎓 {wk['title']}</h3>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div style='text-align: center;'>
                <img src="data:image/gif;base64,{base64.b64encode(open(wk['image'], "rb").read()).decode()}" width="800">
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <p style='text-align: center; font-family: "Libre Baskerville", serif; font-size: 16px; margin-top: 20px;'>
                {wk['desc']}
            </p>
        """, unsafe_allow_html=True)

        st.markdown("""
                <style>
                .button-row {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin-top: 30px;
                    flex-wrap: wrap;
                }

                .resource-button {
                    background-color: #dddddd; 
                    color: #1a1a1a;           
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-size: 15px;
                    font-family: "Libre Baskerville", serif;
                    text-decoration: none !important; 
                    transition: background-color 0.3s ease;
                    display: inline-block;
                }

                .resource-button:hover {
                    background-color: #bbbbbb; 
                }
                </style>""", unsafe_allow_html=True)

      
        st.markdown(f"""
            <div class="button-row">
                <a href="{wk['code']}" target="_blank" class="resource-button">💻 Code</a>
                <a href="{wk['video']}" target="_blank" class="resource-button">📽️ Video</a>
                <a href="{wk['slides']}" target="_blank" class="resource-button">📁 Slides</a>
            </div>
        """, unsafe_allow_html=True)

