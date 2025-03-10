FROM python:3.12-slim


WORKDIR /app


COPY pyproject.toml poetry.lock /app/


RUN pip install poetry


RUN poetry config virtualenvs.create false \
    && poetry install --no-dev


COPY . /app


EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.12-slim


WORKDIR /app


COPY pyproject.toml poetry.lock /app/


RUN pip install poetry


RUN poetry config virtualenvs.create false \
    && poetry install --no-dev


COPY . /app


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
