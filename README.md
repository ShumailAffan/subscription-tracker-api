# Subscription Tracker API

A REST API for tracking recurring subscriptions, renewal dates, and spend categories — built with FastAPI and containerized with Docker. This is a backend rebuild of the [Subscription Tracker App](https://github.com/ShumailAffan/subscription-tracker-app) (originally Flutter + Firebase), implemented as a standalone Python service to demonstrate backend API design separate from the mobile client.

## 🚀 Features

- Full CRUD for subscriptions (create, read, update, delete)
- Renewal-window endpoint — returns subscriptions renewing within the next N days
- Auto-generated interactive API docs via Swagger UI (`/docs`)
- SQLite + SQLAlchemy ORM for data persistence
- Fully containerized with Docker for consistent local and deployed environments

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.11 |
| ORM | SQLAlchemy |
| Database | SQLite |
| Validation | Pydantic |
| Server | Uvicorn |
| Containerization | Docker |

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/subscriptions` | Create a new subscription |
| GET | `/subscriptions` | List all subscriptions |
| GET | `/subscriptions/{id}` | Get a single subscription |
| PUT | `/subscriptions/{id}` | Update a subscription |
| DELETE | `/subscriptions/{id}` | Delete a subscription |
| GET | `/subscriptions/upcoming-renewals?days=7` | List active subscriptions renewing within N days |

Full interactive documentation is available at `/docs` once the server is running.

## 🏁 Getting Started

### Prerequisites

- Python 3.11+
- Docker (optional, for containerized run)

### Option 1: Run locally

```bash
git clone https://github.com/ShumailAffan/subscription-tracker-api.git
cd subscription-tracker-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive Swagger UI.

### Option 2: Run with Docker

```bash
docker build -t subscription-tracker-api .
docker run -p 8000:8000 subscription-tracker-api
```

Visit `http://localhost:8000/docs` to confirm it's running identically to the local version.

## 🗂️ Project Structure

```
subscription-tracker-api/
├── app/
│   ├── main.py       # FastAPI app and route definitions
│   ├── models.py     # SQLAlchemy ORM models
│   ├── schemas.py     # Pydantic request/response schemas
│   ├── crud.py        # Database operations
│   └── database.py    # DB engine and session config
├── requirements.txt
├── Dockerfile
└── README.md
```

## 📄 License

This project is licensed under the MIT License.
