from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api import auth , department,contract,home,user

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

app.include_router(user.router, prefix="/user", tags=["user"])

app.include_router(home.router, prefix="/home", tags=["home"])

app.include_router(contract.router, prefix="/contract", tags=["contract"])

app.include_router(department.router, prefix="/department", tags=["department"])




@app.get("/")
async def read_root():
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
