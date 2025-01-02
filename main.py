import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine, Base
from todo.routers import comment as comment_router
from todo.routers import dashboard as dashboard_router
from todo.routers import role as role_router
from todo.routers import status as status_router
from todo.routers import task as task_router
from todo.routers import user as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost:3000",  # Next.js (локальная разработка)
    "http://127.0.0.1:3000", # Альтернативный локальный домен
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Разрешённые источники
    allow_credentials=True,          # Разрешить отправку cookie
    allow_methods=["*"],             # Разрешённые методы: GET, POST, DELETE и т.д.
    allow_headers=["*"],             # Разрешённые заголовки: Authorization, Content-Type и т.д.
)

app.include_router(task_router.router, prefix='/task')
app.include_router(status_router.router, prefix='/status')
app.include_router(dashboard_router.router, prefix='/dashboard')
app.include_router(comment_router.router, prefix='/comment')
app.include_router(role_router.router, prefix='/role')
app.include_router(user_router.router, prefix='/user')

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True, workers=3)
