FROM python:3.8-slim

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . .

EXPOSE 80

CMD ["streamlit", "run", "main.py", "--server.port", "80"]