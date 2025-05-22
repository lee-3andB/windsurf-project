from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Set up template engine
templates = Jinja2Templates(directory="templates")

# Serve static HTML templates
@app.get("/", response_class=HTMLResponse)
def welcome(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # Placeholder logic — we’ll wire this up to Supabase later
    if username == "admin" and password == "admin":
        return RedirectResponse("/", status_code=303)
    return {"error": "Invalid login"}

@app.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    # Placeholder for sign-up logic
    return RedirectResponse("/", status_code=303)
