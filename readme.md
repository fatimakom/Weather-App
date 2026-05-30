# 🌦️ Aether Weather App

> A clean weather app built with Python & vanilla JS — powered by **OpenWeatherMap API**.

---

## ✨ Features

- 🌍 Real-time weather for any city in the world
- 🌡️ Temperature, humidity, wind speed, visibility
- 💡 Smart daily tips (what to wear, bring umbrella, etc.)
- 🖥️ Terminal (CLI) interface
- 🌐 Beautiful web interface — no framework needed
- 🔑 Only **one** free API key required

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get your free API key

Sign up at [openweathermap.org](https://openweathermap.org/api) — it's 100% free.

Then rename `.env.example` to `.env` and add your key:

```bash
cp .env.example .env
```

```env
OPENWEATHER_API_KEY=your_key_here
```

### 4. Run the CLI app

```bash
python weather.py
```

### 5. Run the Web app

Open `index.html` in your browser and replace `YOUR_OPENWEATHER_API_KEY` in the script tag.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **OpenWeatherMap API** — live weather data
- **Vanilla HTML / CSS / JS** — no frameworks

---

## 💡 How the Tips Work

No AI needed! The app uses simple logic:

| Temperature | Tip |
|---|---|
| 35°C+ | Stay hydrated, avoid sun |
| 25–35°C | Light clothes |
| 15–25°C | Light jacket |
| 5–15°C | Wear a coat |
| Below 5°C | Heavy layers |

Rain or wind detected? Extra tips are added automatically.

---

## 🙋 Author

Built by **Fatima koumayha** — junior developer learning to build with APIs.

- GitHub: [@fatima koumayha](https://github.com/fatimakom/Weather-App.git)
- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
