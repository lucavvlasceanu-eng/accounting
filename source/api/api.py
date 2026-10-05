from pathlib import Path

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent


@app.get("/", response_class=HTMLResponse)
def read_root():
    HTML_PATH = BASE_DIR / "front-end" / "login-page.html"
    if not HTML_PATH.is_file():
        raise HTTPException(status_code=404, detail="Page not found")
    return HTMLResponse(content=HTML_PATH.read_text(encoding="utf-8"))


@app.exception_handler(500)
async def custom_500_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred."},
    )

# @app.get("/users", response_model="UserResponse")
# def return_users(db: Session = Depends(get_db)):
#     users = query.get_all_users(db)
#
#     if users is None:
#         raise HTTPException(
#             status_code=404,
#             detail="There are no users in the database"
#         )

# @app.get("/get_trains", response_model="Train schedule")
# def get_train_schedule(db: Session = Depends(get_db)):
#     trains = query.get_train_schedule()
