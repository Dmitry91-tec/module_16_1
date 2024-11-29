from fastapi import FastAPI

app = FastAPI()


@app.get("/")                                     #get запрос и выполнении функции при его вызове
async def welcome() -> dict:                      #возвращаемый тип данных - словарь
    return {"message": "Главная страница"}        #

@app.get("/user/admin")                                        #get запрос и выполнении функции при его вызове
async def news() -> dict:                                      #возвращаемый тип данных - словарь
    return {"message": f"Вы вошли как администратор"}

@app.get("/user/{user_id}")                                    #get запрос и выполнении функции при его вызове
async def user_id(user_id: str) -> dict:     #возвращаемый тип данных - словарь
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_paginator(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username},Возраст: {age}"}



#запрсы
# Get   - адрес в строке ? переменная=значение
# Post - формы - офрмитьзаказ в магазине
# Put - заменить
# Delete - удалить
