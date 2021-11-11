FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY api/requirements.txt /tmp/
RUN pip install pip
RUN pip install -r /tmp/requirements.txt

COPY ./api /app
