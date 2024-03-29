from uuid import UUID
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("d4af3d86-1beb-49ed-b8eb-41340fa7476a"),
        first_name="Ana",
        last_name="Lobato",
        email="ana@gmail.com",
        role=[Role.role_1],
    ),
    User(
        id=UUID("b7e581b0-f389-4945-9da6-b3cde469e488"),
        first_name="Cleo",
        last_name="Patra",
        email="cleo@gmail.com",
        role=[Role.role_2],
    ),
    User(
        id=UUID("02d78dea-ad98-4a14-8ef2-9b3e38165f84"),
        first_name="Hévelin",
        last_name="Lima",
        email="email@gmail.com",
        role=[Role.role_3],
    ),
]


@app.get("/")
async def root():
    return {"message": "Hello, WoMakers!"}


@app.get("/api/users")
async def get_users():
    return db


@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}


@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}


# HTTP PUT REQUESTS
@app.put("/api/users/{id}")
async def update_user(id: UUID, updated_user: User):
    for i, user in enumerate(db):
        if user.id == id:
            db[i] = updated_user
            return {"message": f"User {id} foi atualizado com sucesso."}
    raise HTTPException(
        status_code=404, detail=f"Usuário com o id: {id} não encontrado."
    )


@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"Usuário com o id: {id} não encontrado."
    )
