from typing import Optional
import uvicorn
from fastapi import FastAPI, Query, HTTPException
from app.models.data_model import Locale, Domain
from app.services.data_service import user_data

app = FastAPI()


@app.get(path="/user_data",
         tags=["User data"],
         description="Эндпоинт генерирует случайные данные пользователя, включая имя, фамилию и email-адрес. "
                     "Локализация влияет на формат имени и фамилии, а домен — на email.",
         response_description="Возвращает JSON с именем, фамилией и email-адресом",
         responses={
             200: {
                 "description": "Успешный ответ с сгенерированными данными",
                 "content": {
                     "application/json": {
                         "example": {
                             "first_name": "Иван",
                             "last_name": "Петров",
                             "email": "ivan_petrov@mail.ru"
                         }
                     }
                 }
             },
             400: {
                 "description": "Некорректные параметры (например, неверная локализация или домен)"
             }
         }
         )
def generate_user_data_endpoint(
        locale: Optional[Locale] = Query(default=None, description="Локализация:"),
        domain: Optional[Domain] = Query(default=None, description="Домен для email:")
):
    try:
        locale_value = locale.value if locale else None
        domain_value = domain.value if domain else None

        email, first_name, last_name = user_data(domain=domain_value, locale=locale_value)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
