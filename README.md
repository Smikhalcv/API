# Сервер Джанго

## Инструкция по установке:
**После клонирования репозитория прописать следующие команды в терминале из соответствующего каталога:**
(Необходимо установить Python - написан на версии 3.8.6)

Для управления окружением в проектe используется [pipenv](https://pipenv.pypa.io/en/latest/).
Если [pipenv](https://pipenv.pypa.io/en/latest/) не установлен, установить:

- MacOS: `brew install pipenv`,

- Linux: `sudo pip install pipenv`,

- Windows: `pip install pipenv`

Затем 
- `pipenv install --dev` - Создание нового виртуального окружения и установка зависимостей.
- `pipenv run init` -   установка pre-commit скриптов

### Структура проекта:

 - `/.github`
   - `/.workflows` - настройки git actions
      - `cz_bump.yml` - конфиг автоматического версионирования
      - `python-app.yml` - конфиг линтеров и тестирования приложения
 - `/src` - рабочий каталог, содержит код сервера django
   - `/config` - основной проект django 
   - `/main_app` - основное приложение (было `sheduliZZZer` переименовал для большей гибкости) 
   - `/static` - статика
   - `manage.py` 
   - `utils.py` 
 - `.editorconfig` - настройки ide, требует установки соответствующего плагина ([download page](https://editorconfig.org/#download))
 - `.env` - необходимо создать. **Должен присутствовать в .gitignore!** Содержит используемые для работы переменные (об этом ниже).
   Доступ к переменным из кода получаем с помощью `os.enveron.get('var_name',default_value)`
 - `.gitatributes` - настройки поведения клиента git ([зачем это здесь?](https://htmlacademy.ru/blog/boost/tools/konec-stroki), [документация](https://git-scm.com/docs/gitattributes))
 - `.gitignore`
 - `.pre-commit-config.yml` - настройка pre-commit ([документация](https://pre-commit.com/))
 - `Pipfile` - настройки pipenv, описание зависимостей и тд(заменяет файл requirements.txt). 
 - `Pipenv.lock` - хранит версии используемых пакетов и их зависимостей
 - `pyproject.toml` - хранит настройки некотрых пакетов
 - `readme.md` - этот файл

### Переменные окружения
Также в корне проекта необходимо создать файл **.env** со следующими переменными:

Обязательно:
- `SECRET_KEY` - cекретный ключ Django
- `PYTHONPATH` - путь к корню Django проекта сейчас это `./src/`

Если используем Postgres:
- `POSTGRES` - для использования Postgres устанавливаем значение `on`.
  если переменная отсутствует, либо имеет любое другое значение, например `off` будет использоваться Sqlite.
- `POSTGRES_DB` - название базы данных
- `POSTGRES_USER` - имя пользователя
- `POSTGRES_PASSWORD` - пароль
- `POSTGRES_HOST` - хост, для localhost: 127.0.0.1
- `POSTGRES_PORT` - порт по умолчанию: 5432

Пример содержимого файла **.env**:
  ```
  SECRET_KEY=+k*ppm$q7*z&1lc36u$mb4ttm_c32_gey5xbrhgq@f!9dfyfhygvh
  PYTHONPATH=./src/
  POSTGRES=on
  POSTGRES_DB=sh_db
  POSTGRES_USER=sh_user
  POSTGRES_PASSWORD=password
  POSTGRES_HOST=127.0.0.1
  POSTGRES_PORT=5432
  ```

### config/settings.py
В config/settings реализован автоматический выбор настроек БД (переменная POSTGRES, в файле .env). Настройки Postgres тоже берутся из файла `.env`

На этом приготовления закончены, для запуска прописать команду:
-  `pipenv run serve`

Итак:
БД - для использования PostgeSQL - установить переменную в .env POSTGRES=on.

Поставил джанго дебаг.

Ipython - мне понравился.

Пока при запуске выкидивает 404 ошибку, поскольку сервер голый и нет привязак к урлам. 
Все шаблоны, согласно настройкам должны находиться в `templates/main_app`, css и js файлы в папке `static/css|/js
` соответственно.


## Использование

Для активации виртуального окружения используется команда 
- `pipenv shell` - Команда активирует виртуальное окружение и подгружает переменные из файла `.env` в корне проекта.

Рабочий процесс происходит приблизительно так:
- `pipenv shell` - активация окружения
- пишем код
- `git status` покажет что наизменяли
- `git add` добовляет изменения в коммит
- `cz commit` ([commitizen-tool](https://commitizen-tools.github.io/commitizen/)) фиксирует изменения(вместо git commit). **Сообщения коммитов пойдут в changelog.md!**
  Запускает pre-commit проверки
- Если pre-commit отработал нормально, отправляем в репо `git push`
- далее редактируем ...
  
Иногда возникает потребность выти из виртуального окружения. Для выхода из окружения можно использовать команду `exit`

Если нужно выполнить одну команду в виртуальном окружении c последующим выходом из него, возможно использовать
- `pipenv run < comands >`

Как пример: 
- `pipenv run lint` - выполнит команду `lint` содержащеюся в секции scripts в Pipenv файле.
    
Доступные команды:
- `pipenv run init` - инициализация pre-commit скриптов
- `pipenv run manage` - Dgango manage.py
- `pipenv run lint` - проверка стиля написания кода ([flake8](https://flake8.pycqa.org/en/latest/), [rules](https://www.flake8rules.com/))
- `pipenv run fix` - исправление стилистических ошибок - запустит [black](https://black.readthedocs.io/en/stable/)
- `pipenv run test` - запуск связки [pytest](https://docs.pytest.org/en/stable/), [pytest-django](https://pytest-django.readthedocs.io/en/latest/) и [coverage](https://coverage.readthedocs.io/en/coverage-5.3/)
- `pipenv run serve` - тоже что и `python3 ./src/manage.py runserver`,запуск сервера

Кроме этого через `pipenv run` - можно запустить любую другую команду и она выполнится в виртуальном окружении.


Пока всё что мог, дальше будем продвигать. Если что не так сделал говорите! =)
