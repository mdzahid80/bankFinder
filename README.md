# Bank API branch detail finder

<details>
  <summary><strong>Bank Finder</strong></summary>
  


## **BankFinder: Django API server to fetch bank details**

This project is a Django-based API that allows users to search for bank accounts based on branch names. The data is stored in a CSV file and is loaded into memory for searching.

### Features

- Search for bank accounts by branch name
- Return all rows containing the specified branch name
- Simple and easy-to-use API

### Requirements

- Python 3.x
- Django
- Pandas

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mdzahid80/bankFinder.git
   cd bank-account-search-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the Django project:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### **Testing**

1. Open Postman and create a new HTTP request for each of the REST API endpoints.
2. Send requests to the endpoints to test the API details
3. Verify that the responses are correct and the data fetch is according to requirements.

## Usage

1. **Upload the CSV file:**
   - Place your CSV file in the project directory. Ensure the file is named `bank_branches.csv`.

2. **Run the server:**
   ```bash
   python manage.py runserver
   ```

3. **Search for bank accounts:**
   - Use the following endpoint to search for bank accounts by branch name:
     ```
     GET http://127.0.0.1:8000/finder/search/?keyword=branch_name
     ```

## Example

To search for bank accounts in the "Delhi" branch, use the following URL:
```
http://127.0.0.1:8000/finder/search/?keyword=Delhi
```

## Project Structure

```
bank-account-search-api/
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── finder/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── data.csv
├── manage.py
└── requirements.txt
```

