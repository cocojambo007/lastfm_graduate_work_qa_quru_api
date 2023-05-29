# Автотесты для сайта

* https://reqres.in/api/

* API тесты
  * ✅ Регистрация нового пользователя
  * ✅ Получение информации об одном пользователе
  * ✅ Получение информации о нескольких пользователях
  * ✅ Обновление информации о пользователе
  * ✅ Удаление информации о пользователе

  
## Технологический стек
<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="resources/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="resources/logo/Github.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/Jenkins.png"></code>
  <code><img width="5%" title="selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure.png"></code>
<!--   <code><img width="5%" title="Jira" src="resources/logo/jira.png"></code> -->
  <code><img width="5%" title="Telegram" src="resources/logo/tg.png"></code>
</p>

## <img width="6%" title="Jenkins" src="resources/logo/Jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/lastfm_graduate_work_qa_quru_api/)

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Собрать сейчас"

<p><img src="resources/screenshots/chrome_ENhzCr3tLM.png" alt="Jenkins"/></p>

## Запуск тестов
### Локально
```
pytest .
```

### Удаленно
```bash
rm -rf allure-results/*
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --alluredir=allure-results
```

### <img width="6%" title="Allure" src="resources/logo/allure.png"> [Allure](https://jenkins.autotests.cloud/job/lastfm_graduate_work_qa_quru_api/2/allure/)

#### Примеры отображения тестов

<img src="resources/screenshots/chrome_fGyPY1veXE.png" alt="Allure"/>

<img src="resources/screenshots/chrome_yUJoSgOnCX.png" alt="Allure"/>

### <img width="6%" title="Telegram" src="resources/logo/tg.png"> Telegram

#### Настроена отправка отчета в Telegram

<img src="resources/screenshots/Telegram_Pwv1wed5bx.png" alt="Telegram"/>

