# HackerNews API Test Framework

A lightweight API testing framework for the [HackerNews public API](https://github.com/HackerNews/API) using Python, `pytest`, and `requests`.

---

## Basic Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/hackernews-api-tests.git
cd hackernews-api-tests
```


### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Tests

### Run all tests

```bash
pytest
```

### Run a specific test file

```bash
pytest tests/test_items_api.py
```

## Tech Stack

- Python 3.8+
- pytest
- requests