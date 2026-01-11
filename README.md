# ✍️ Handwritten Assignment Generator

## 📌 Description

The **Handwritten Assignment Generator** is a Flask-based web application that converts typed text into realistic handwritten-style assignments. Users can select from multiple handwriting fonts, generate multi-page handwritten images, and download the final output as a **PDF document**.

This project demonstrates **Python backend architecture, image processing, PDF generation, and Flask web development**, making it suitable for academic use, automation tasks, and portfolio projects.

---

## 🚀 Features

* Convert text into handwritten-style pages
* Multiple handwriting font styles (dropdown selector)
* Automatic multi-page handling
* Export handwritten assignment as PDF
* Clean and responsive web interface
* Modular backend design (service-based architecture)

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask** – Web framework
* **Pillow (PIL)** – Image and font rendering
* **ReportLab** – PDF generation
* **HTML & CSS** – Frontend UI
* **Gunicorn** – Production server (deployment)

---

## 📂 Project Structure

```
handwritten-assignment-flask/
│
├── app.py
├── config.py
├── handwriting_service.py
├── utils.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── fonts/
│   │   ├── PatrickHand.ttf
│   │   ├── Caveat.ttf
│   │   └── DancingScript.ttf
│   │
│   └── output/
│       ├── page_1.png
│       └── assignment.pdf
│
└── templates/
    └── index.html
```

---

## ⚙️ Local Setup & Run Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/handwritten-assignment-flask.git
cd handwritten-assignment-flask
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## ✍️ How It Works

1. User enters assignment text in the textarea
2. Selects a handwriting font style
3. Backend converts text into handwritten images using Pillow
4. Images are compiled into a multi-page PDF using ReportLab
5. User downloads the final handwritten assignment

---

## 🔧 Important Code Configuration

### Font Configuration (`config.py`)

Fonts are managed using a centralized dictionary:

```python
FONTS = {
    "patrick": "static/fonts/PatrickHand.ttf",
    "caveat": "static/fonts/Caveat.ttf",
    "dancing": "static/fonts/DancingScript.ttf",
}
```

This design allows easy addition of new handwriting styles.

---



