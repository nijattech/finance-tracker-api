# 💳 Finance Tracker REST API

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Protected-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

An asynchronous RESTful API for personal finance tracking, category management, and automated financial analytics. Built with Python 3.13 and FastAPI using Clean Architecture principles.

---

## 🛠 Tech Stack

* **Core Framework:** Python 3.13, FastAPI
* **Database & ORM:** SQLite (Async Engine), SQLAlchemy 2.0
* **Database Migrations:** Alembic
* **Data Validation:** Pydantic v2
* **Authentication & Security:** JWT (OAuth2 Password Bearer), Passlib (Bcrypt hashing)

---

## 🚀 Key Features

* **User Authentication:** Registration, login, password hashing, and OAuth2 JWT authentication.
* **Category Management:** Create and list user-specific spending/income categories.
* **Transactions System:** Record income/expenses with category association and URL filters.
* **Analytics Engine:** Instant summary calculation (total income, expenses, net balance).

---

## 📌 API Endpoints Overview

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `POST` | `/auth/register` | Register a new user | ❌ |
| `POST` | `/auth/login` | Log in & get JWT access token | ❌ |
| `GET` | `/categories/` | List current user categories | 🔒 |
| `POST` | `/categories/` | Create new category | 🔒 |
| `GET` | `/transactions/` | Get filtered transactions list | 🔒 |
| `POST` | `/transactions/` | Create income/expense entry | 🔒 |
| `GET` | `/stats/summary` | Get balance & financial analytics | 🔒 |

---

## 📁 Project Structure

```text
finance_tracker/
├── alembic/              # Database migration scripts
├── app/
│   ├── api/              # API routers (auth, categories, transactions, stats)
│   ├── core/             # Configuration, database setup, security & CRUD
│   ├── models/           # SQLAlchemy DB models
│   ├── schemas/          # Pydantic schemas (data validation)
│   └── main.py           # Application entry point
├── .gitignore            # Excluded git files
├── alembic.ini           # Alembic config
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies