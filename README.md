### Проект автоматизации тестирования UI сайта
___
![Python](https://img.shields.io/pypi/pyversions/pip?color=g&label=Python%20version&style=plastic)
![pip](https://img.shields.io/pypi/v/pip?style=plastic)
___
_Цели:_
1. Применить паттерн *Page Object* и фреймворк *Pytest* для автоматизации тестирования.
2. Закрепить навыки выбора уникальных CSS селекторов.
3. Использовать возможность остановки теста при падении предыдущего.
4. Совместить в `conftest.py` выбор браузера и языков для тестируемого сайта.
5. Разобрать некоторые возможности плагина *pytest-html*.
6. Выполнить и разместить отчет о тестировании.
___
Установка версий:

```python
pip install -r requirements.txt
```
___
Информация:

Для работы проекта необходимо установить `chromedriver` и `geckodriver`.

Документация Selenium на [сайте](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).

По умолчанию запуск тестов выполняется в браузере *Chrome* с русским языком сайта.

Запуск тестов с выбором браузера и языка:

```python
pytest --browser_name=firefox test_main_page.py
pytest -v --browser_name=firefox
pytest -v --language=en
```
В настройках отчета в `conftest.py` удалена информация об операционной системе:

```python
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Platform", None)
```
Запуск с выполнением отчета ( html-файл можно открыть в браузере ):

```python
pytest --html=report_file.html
```
___

Screenshot

![screenshot](https://github.com/ProgRiver/website_page_autotest_project/blob/main/assets/rep.png)
