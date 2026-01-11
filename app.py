from flask import Flask, render_template, request, send_file
from handwriting_service import generate_handwritten_pages, generate_pdf
from utils import ensure_output_dir

app = Flask(__name__)
ensure_output_dir()

@app.route("/", methods=["GET", "POST"])
def index():
    pdf_ready = False

    if request.method == "POST":
        text = request.form.get("text")
        font_choice = request.form.get("font")

        if text:
            images = generate_handwritten_pages(text, font_choice)
            generate_pdf(images)
            pdf_ready = True

    return render_template("index.html", pdf_ready=pdf_ready)


@app.route("/download")
def download():
    return send_file("static/output/assignment.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
