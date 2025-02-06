from fastapi import FastAPI
from services.data_service import generate_email

app = FastAPI()


@app.get("/generate_email/{domain}/{locale}")
def generate_email_endpoint(domain: str, locale: str):

    email = generate_email(domain=domain, locale=locale)
    return {"email": email}
