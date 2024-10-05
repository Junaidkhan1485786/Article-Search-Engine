from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from passlib.context import CryptContext
from pathlib import Path
import mysql.connector
from mysql.connector import Error
import uvicorn
app = FastAPI()

def create_user_registration_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='user_registration',
            user='root',
            password='junaidkhan1485786'
        )
        print("Successfully connected to MySQL database user_registration")
    except Error as e:
        print(f"Error: '{e}'")
    return connection



@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = Path("static/article.html").read_text()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/register", response_class=HTMLResponse)
async def read_root():
    html_content = Path("static/index.html").read_text()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    html_content = Path("static/login.html").read_text()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/userprofile", response_class=HTMLResponse)
async def login_page():
    html_content = Path("static/profile.html").read_text()
    return HTMLResponse(content=html_content, status_code=200)

# Initialize bcrypt for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(email):
    connection = create_user_registration_connection()
    if connection is not None:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            return user
        except Error as e:
            print(f"Error: '{e}'")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        return None

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    # Retrieve user from database
    user = get_user(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify password
    if not verify_password(password, user['password']):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return RedirectResponse(url="/userprofile", status_code=302)

@app.post("/register")
async def register_user(
        name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        repeat_password: str = Form(...)
):
    # Print form data to console (except password)
    print(f"Received registration data:")
    print(f"Name: {name}")
    print(f"Email: {email}")

    # Validate passwords match (although this is also done client-side)
    if password != repeat_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Hash the password
    hashed_password = pwd_context.hash(password)

    connection = create_user_registration_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            values = (name, email, hashed_password)
            cursor.execute(query, values)
            connection.commit()
            print(f"User {name} registered successfully")
            # Redirect to the /login page
            return RedirectResponse(url="/login", status_code=302)
        except Error as e:
            print(f"Error: '{e}'")
            raise HTTPException(status_code=500, detail=f"Failed to register user: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    else:
        raise HTTPException(status_code=500, detail="Database connection failed")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
# python -m uvicorn main:app --reload --port 8000