import allure
from allure_commons.types import Severity
from pytest_voluptuous import S
from requests import Response
from schemas.schemas import create, single_user, users_list_schema

name = "Pavel"
job = "QA"
json = {
    "name": name,
    "job": job
}


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('API')
@allure.title('Регистрация нового пользователя')
def test_post_create(reqres):
    response: Response = reqres.post(
        'users', json
    )
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert response.status_code == 201
    assert S(create) == response.json()


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('API')
@allure.title('Получение информации об одном пользователе')
def test_get_single_user(reqres):
    response: Response = reqres.get(
        'users/2')
    assert response.status_code == 200
    assert S(single_user) == response.json()


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('API')
@allure.title('Получение информации о нескольких пользователях')
def test_get_list_users(reqres):
    response: Response = reqres.get(
        'users?page=2')
    assert response.status_code == 200
    assert S(users_list_schema) == response.json()


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('API')
@allure.title('Обновление информации о пользователе')
def test_put_update(reqres):
    response: Response = reqres.put(
        'users/2', json)
    assert response.status_code == 200


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('API')
@allure.title('Удаление информации о пользователе')
def test_delete_delete(reqres):
    response: Response = reqres.delete('users/2')
    assert response.status_code == 204
