# 📚 Bookstore API Automation Testing

![WhatsApp Image 2025-05-18 at 17 08 09_5f1fde6e](https://github.com/user-attachments/assets/1f020ae8-c74f-405f-afdf-8c55fddf21c4)


An end-to-end **API Automation Testing Project** built using **FastAPI**, **PyTest**, and **Requests**, simulating a real-world bookstore scenario. This project is designed to demonstrate **test-driven development (TDD)**, **CI/CD integration**, and core **SDET skills**.

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup--Installation](#setup--installation)
- [Running Tests](#running-tests)
- [cicd-with-github-actions](#cicd-with-github-actions)
- [Learning Outcomes](#learning-outcomes)

---

## Project Overview

This is a sample REST API for a bookstore that supports:

- 🔐 User login and token-based authentication
- 📖 Book retrieval and ordering
- ❌ Book deletion
- ✅ Automated testing of all endpoints

It includes a suite of **automated tests** and a **CI pipeline using GitHub Actions** to run the tests on every commit.

---

## Tech Stack

| Technology      | Purpose                            |
|-----------------|------------------------------------|
| `FastAPI`       | Building the backend API           |
| `PyTest`        | Automated API testing              |
| `Requests`      | Sending HTTP requests in tests     |
| `GitHub Actions`| Continuous integration (CI/CD)     |

---

## Project Structure

```bash
bookstore-api/
│
├── app.py # Main API application
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
├── tests/
│ └── test_api.py # PyTest test cases
│
└── .github/
└── workflows/
└── python-tests.yml # GitHub Actions CI workflow
```

---
## Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Karangarg01/BookStore-API-Testing.git
cd BookStore-API-Testing
```
2️⃣ Create virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ Run the API
```bash
uvicorn app:app --reload
```
Access the interactive Swagger docs at: http://localhost:8000/docs

## Running Tests
```bash
pytest tests/
```
The test suite includes:

✅ Login success & failure

✅ Retrieve all books

✅ Place book orders

✅ Delete books with token authentication

---
## CI/CD with GitHub Actions
✅ Tests run automatically on every push to main branch using GitHub Actions.

See: .github/workflows/python-tests.yml

---
## Learning Outcomes
This project demonstrates:

- Writing modular and reusable API tests
- Understanding token-based auth and edge case handling
- Implementing end-to-end integration testing
- Integrating automated testing in a CI/CD pipeline
- SDET mindset: ownership of quality, coverage, and reliability
