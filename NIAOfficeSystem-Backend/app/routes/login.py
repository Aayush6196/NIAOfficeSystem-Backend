from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
