FROM python:3.13-slim

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false

WORKDIR /app

COPY . .

RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "devnotes.main:app", "--host", "0.0.0.0", "--port", "8000"]
