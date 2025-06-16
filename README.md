<h1 align="center">
  🧠 Stress Detection System
</h1>

<p align="center">
  A machine learning web app that predicts stress levels based on sleeping patterns and physiological data.<br>
  Built using <strong>Flask</strong>, <strong>Firebase</strong>, and <strong>Scikit-learn</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-deployed-brightgreen" />
  <img src="https://img.shields.io/github/license/MohdFasi1/stress-detection-system" />
</p>

---

## 🌐 Live Demo

🔗 [https://stress-detection-system.onrender.com](https://stress-detection-system.onrender.com)

---

## ✨ Features

- 🔍 Predicts stress level using real-world sleep parameters
- 🧠 Machine learning model trained on physiological sleep data
- 📱 Responsive and mobile-friendly UI built with Bootstrap
- 📊 Real-time prediction with clear stress level output
- 📁 Clean input form with 8 health features
- 🌐 Easy-to-deploy backend powered by Flask
---
## 🚀 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Firebase-FFCA28?logo=firebase&logoColor=black" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white" />

</p>

---

## 🧩 How It Works

The user inputs 8 health parameters related to sleep:

- 😴 *Snoring Range*
- 🌬️ *Respiration Rate*
- 🌡️ *Body Temperature*
- 🦵 *Limb Movement Rate*
- 🩸 *Blood Oxygen*
- 👁️ *Eye Movement*
- ⏰ *Number of Hours Sleep*
- ❤️ *Heart Rate*

These inputs are passed to a trained machine learning model which predicts one of the following *stress levels*:

- 🟢 *Low/Normal*
- 🟡 *Medium Low*
- 🟠 *Medium*
- 🟠 *Medium High*
- 🔴 *High*

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/MohdFasi1/stress-detection-system.git
cd stress-detection-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Firebase configuration

Create a `.env` file in the root of your project:

```
apiKey=your_api_key
authDomain=your_auth_domain
projectId=your_project_id
storageBucket=your_storage_bucket
messagingSenderId=your_messaging_sender_id
appId=your_app_id
measurementId=your_measurement_id
```

### 4. Run the server locally

```bash
python app.py
```

Or for production:

```bash
gunicorn app:app
```

---

## 🌍 Deployment

To deploy:

1. Add `.env` values in environment tab.
2. Ensure `gunicorn` is in your `requirements.txt`.
3. Set the start command to:

```bash
gunicorn app:app
```

---

## 📁 Project Structure

```
├── app.py
├── model
|   ├── dataPreprocess.ipynb
|   ├── model_Generator.ipynb
|   └── stress_model.pkl
├── templates/
│   ├── index.html
│   ├── prediction.html
│   └── ...
├── static/
│   ├── css
│   ├── js
│   └── ...
├── data/
│   └── stress_dataset.csv
├── .env
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 Author

**Mohd Fasi**  
🔗 GitHub: [MohdFasi1](https://github.com/MohdFasi1)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
