FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app

COPY ./data/kjfacts.csv /data/kjfacts.csv
