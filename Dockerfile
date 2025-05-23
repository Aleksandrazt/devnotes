FROM python:3.13-slim

WORKDIR /app

RUN pip install poetry

# Копируем зависимости и устанавливаем их
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
 && poetry install --no-root

# Копируем весь проект
COPY . .
CMD ["poetry", "run", "uvicorn", "devnotes.main:app", "--host", "0.0.0.0", "--port", "8000"]
