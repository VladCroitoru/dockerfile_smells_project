FROM python:3.8

COPY requirements.txt app/

WORKDIR app/

RUN pip install -r requirements.txt

COPY src/ /app

ENV PORT 8050

CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 app:server

# CMD exec python3 app.py
