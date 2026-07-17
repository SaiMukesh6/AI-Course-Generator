import os
from dotenv import load_dotenv
from groq import Groq

# ---------------- LOAD ENV ---------------- #

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# ==========================================================
#               GENERATE COURSE
# ==========================================================

def generate_ai_course(topic, difficulty, modules, reading_time, language):

    prompt = f"""
You are an expert educator and course designer.

Your task is to generate a professional course.

Course Details:

Topic: {topic}
Difficulty: {difficulty}
Number of Modules: {modules}
Reading Time per Module: {reading_time}
Language: {language}

Generate the course in the following format.

# Course Title

## Course Overview

Write a short introduction about the course.

## Learning Objectives

Provide 5 learning objectives.

Create exactly {modules} modules.

For every module include:

# Module Number and Module Title

## Topics Covered

Mention 3 to 5 important topics.

## Explanation

Explain every topic in simple language. If the topic is technical, scientific, or programming-related, you MUST include relevant code snippets, terminal commands, or syntax examples formatted in proper markdown code blocks (e.g., using ```python or ```bash).

## Practical Example

Give one real-life example. If the topic is technical, provide a hands-on code sample or command-line demonstration illustrating the concept.

## Real World Application

Explain where this concept is used.

## Key Takeaways

Give 3 important points.

After completing all modules include:

# Final Summary

Summarize the complete course.

# Interview Questions

Generate 5 interview questions with short answers.

Use proper Markdown headings.

Make the output neat and professional.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0.7,

        messages=[
            {
                "role": "system",
                "content": "You are a professional educator and curriculum designer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content


# ==========================================================
#               CHAT WITH GENERATED COURSE
# ==========================================================

def chat_with_course(course, question):

    prompt = f"""
You are an AI Tutor.

Below is a generated course.

----------------------------

{course}

----------------------------

Answer the user's question ONLY using the generated course.

If the answer is not available in the generated course,
reply exactly:

"I couldn't find that information in the generated course."

Question:

{question}

Answer:
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0.4,

        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI tutor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content