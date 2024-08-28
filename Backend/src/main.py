from fastapi import FastAPI
import uvicorn
from config import settings
from fastapi.middleware.cors import CORSMiddleware
from api import auth
from api import contract
from api import home




app = FastAPI(
    title='PointOfSell',
    description='FastApi PointOfSell Project',
    version='1.0.0',
    docs_url='/',
)
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/auth", tags=["auth"])

app.include_router(home.router, prefix="/home", tags=["home"])

app.include_router(contract.router, prefix="/contract", tags=["contract"])




@app.get("/")
async def read_root():
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
