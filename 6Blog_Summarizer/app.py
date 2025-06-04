from flask import Flask, request, render_template
import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set API key for the new OpenAI SDK
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    error = ""
    if request.method == "POST":
        blog_text = request.form.get("blog_text", "").strip()

        if blog_text:
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You summarize blog posts in a concise way."},
                        {"role": "user", "content": f"Summarize the following:\n{blog_text}"}
                    ],
                    temperature=0.7,
                    max_tokens=300
                )
                summary = response.choices[0].message.content
            except Exception as e:
                error = f"❌ API Error: {str(e)}"
        else:
            error = "⚠️ Please enter some blog text to summarize."

    return render_template("index.html", summary=summary, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
