from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 🛡️ Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por ["http://localhost:5173"] si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👤 Modelo de usuario
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

# 🧠 Base de datos temporal en memoria
users: List[User] = []
next_id = 1

# 🚀 Rutas CRUD
@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(user: User):
    global next_id
    user.id = next_id
    users.append(user)
    next_id += 1
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for i, u in enumerate(users):
        if u.id == user_id:
            updated_user.id = user_id
            users[i] = updated_user
            return updated_user
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u.id != user_id]
    return {"message": "User deleted"}
