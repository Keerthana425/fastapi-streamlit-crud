# Employee Management CRUD App

A full-stack CRUD application built using FastAPI, Streamlit, and MySQL to manage employee records through REST APIs and an interactive user interface.

## Features

* Add employees
* View employee records
* Update employee details
* Delete employees
* REST API using FastAPI
* Interactive frontend using Streamlit
* MySQL database integration

## Tech Stack

* Python
* FastAPI
* Streamlit
* MySQL
* Uvicorn
* Requests Library

## Project Structure

```text id="4g2fyy"
API_CRUD/
│
├── main.py          # FastAPI backend
├── app.py           # Streamlit frontend
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash id="d2n0e4"
git clone https://github.com/your-username/fastapi-streamlit-crud.git
cd fastapi-streamlit-crud
```

### 2. Create Virtual Environment

```bash id="9ty4yq"
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash id="ng9m56"
venv\Scripts\activate
```

#### Mac/Linux

```bash id="6f0f7q"
source venv/bin/activate
```

### 4. Install Dependencies

```bash id="i7d3fg"
pip install -r requirements.txt
```

Or manually install:

```bash id="39sn4n"
pip install fastapi uvicorn streamlit mysql-connector-python requests
```

## MySQL Table

```sql id="f1xyo5"
CREATE TABLE emp(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(50),
    department ENUM(
        'dev',
        'test',
        'aws',
        'devops',
        'ai/ml engineer',
        'gen-ai'
    ) DEFAULT 'test'
);
```

## Run FastAPI Server

```bash id="23v3br"
uvicorn main:app --reload
```

Server runs at:

```text id="zpbmvg"
http://127.0.0.1:8000
```

Swagger API Docs:

```text id="9pqtnm"
http://127.0.0.1:8000/docs
```

## Run Streamlit App

```bash id="b3d68k"
streamlit run app.py
```

Frontend runs at:

```text id="lskp3r"
http://localhost:8501
```

## API Endpoints

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| GET    | `/workers`            | Get all employees |
| POST   | `/add_worker`         | Add employee      |
| PUT    | `/update_worker/{id}` | Update employee   |
| DELETE | `/delete_worker/{id}` | Delete employee   |

## Example Employee JSON

```json id="7z42by"
{
  "name": "Keerthana",
  "email": "keerthana@gmail.com",
  "department": "gen-ai"
}
```

## Future Improvements

* Authentication and Login
* Search and Filter
* Pagination
* Docker Deployment
* Cloud Database Integration

## Author

Keerthana Reddy
