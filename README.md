# 🔥 Flask + Redis App (Dockerized)

This is a simple Python **Flask** application that uses **Redis** to store and retrieve a counter value. It's fully **Dockerized** using **Docker Compose** to run both services together seamlessly.

Perfect for learning how Flask and Redis work together, and how to orchestrate multiple services using Docker Compose.

---

## 📦 Features

- Lightweight Flask web server
- Uses Redis to store a simple counter
- Dockerized for easy setup
- Multi-container orchestration using Docker Compose
- Auto-reloads Flask app on code change (development-friendly)

---

## 🧠 How It Works

1. The Flask app connects to the Redis service.
2. Every time you refresh the page, a counter in Redis is incremented.
3. The updated count is displayed in the browser.

---

## 📁 Project Structure

Flask-Redis-App/
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Flask Docker image
├── docker-compose.yml # Compose file for Flask + Redis
└── README.md # Project documentation


---

## 🚀 Getting Started

### 🐳 Step 1: Run with Docker Compose

```bash
docker-compose up --build
````

This will:

Build the Flask app image

Pull the Redis image

Start both services

🌐 Step 2: Visit in Browser
Go to:
http://localhost:5000

You should see:
```
Hello! You have visited this page X times.
```

<img width="960" alt="image" src="https://github.com/user-attachments/assets/1fb17021-365e-4ece-8a58-bf6749ad7dff" />


📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Shreya Khanduri Bhatt
