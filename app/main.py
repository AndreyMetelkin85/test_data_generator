import uvicorn
from fastapi import FastAPI, Query, HTTPException
from app.models.data_model import Locale, Domain
from app.services.data_service import generate_email

app = FastAPI()


@app.get(path="/generate-email", tags=["Emails"], description="Создание почты")
def generate_email_endpoint(
        locale: Locale = Query(default=Locale.en_US, description="Локализация:"),
        domain: Domain = Query(default=Domain.GMAIL, description="Домен для email:")
):
    try:
        email = generate_email(domain=domain.value, locale=locale.value)
        return {"email": email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
