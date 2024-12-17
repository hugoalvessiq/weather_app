# Weather App 🌤️

This is a learning project that consumes the **open API** from [Open-Meteo](https://open-meteo.com/) to provide simple, real-time weather information.

The goal is to explore web development concepts with **Python Flask**, API consumption, and the creation of simple interfaces using **HTML** and **CSS**.

---

## 🚀 Features

- Search for weather information for any city.
- Displays temperature, weather condition, and recording time.
- Simplified icons using **Google Material Icons**.
- Consumption of an open API (Open-Meteo).

---

## 📦 Technologies Used

- **Python** (Backend)
- **Flask** (Web Framework)
- **HTML/CSS** (Frontend)
- **Google Material Icons** (Interface Icons)
- **Open-Meteo** (Free weather data API)

---

## ⚙️ Environment Setup

### Prerequisites

- Python 3.10+
- Pip (Python package manager)

### Step by Step

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/hugoalvessiq/weather-app.git](https://github.com/hugoalvessiq/weather-app.git)
   cd weather-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` ile for environment variables (optional):**

   ```bash
   touch .env
   ```

   **Example of `.env` (if needed):**

   ```
   FLASK_ENV=development
   ```

5. **Run the Flask application:**

   ```bash
   flask run
   ```

6. **Access in the browser:**
   ```
   http://127.0.0.1:5000
   ```

## 📚 Dependencies

All dependencies are listed in  `requirements.txt`:

```txt
attrs==24.2.0
blinker==1.9.0
cattrs==24.1.2
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
Flask==3.1.0
flatbuffers==24.3.25
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
numpy==2.2.0
openmeteo_requests==1.3.0
openmeteo_sdk==1.18.0
pandas==2.2.3
platformdirs==4.3.6
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.2
requests==2.32.3
requests-cache==1.2.1
retry-requests==2.0.0
six==1.17.0
tzdata==2024.2
url-normalize==1.4.3
urllib3==2.2.3
waitress==3.0.2
Werkzeug==3.1.3
```

---

## 🧩 Project Structure

```
weather-app/
│
├── static/
│   └── styles/
│       └── styles.css         # CSS File
│
├── templates/
│   └── index.html             # HTML Template
│
├── .env                       # Environment variables (optional)
├── app.py                     # Main Flask application
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation
```

---

## 🌐 Data Source

The weather data is provided by [Open-Meteo](https://open-meteo.com/), an open API that does not require an API key.

---

## 🎯 Project Goal

This project was developed for the purpose of **learning** and **practicing** concepts of:

- Web development with Flask.
- Open API consumption.
- Backend data manipulation.
- Python project structuring.
- Creating simple interfaces with HTML and CSS.

---

## 🤝 Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to open an **issue** or submit a **pull request**.

---

## 📜 License

This project is under the **MIT** license. See the `LICENSE` file for more information.

---

## 💡 Author

Developed by [Hugo/hugoalvessiq](https://github.com/hugoalvessiq).

---

I hope this project helps you learn more about web development and APIs! 🚀

---
