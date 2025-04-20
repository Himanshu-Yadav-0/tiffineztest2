from fastapi import FastAPI
from app.api import user_routes
from app.api import tiffin_routes,subscription_routes
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to NourishX!"}

app.include_router(user_routes.router)
app.include_router(tiffin_routes.router)
app.include_router(subscription_routes.router, prefix="/subscriptions", tags=["Subscriptions"])

