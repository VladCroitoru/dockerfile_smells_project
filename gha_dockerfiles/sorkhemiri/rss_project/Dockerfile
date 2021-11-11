FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

LABEL author="Mahdi Sorkhemiri <Sorkhemiri@gmail.com>"


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VARIABLE_NAME app
ENV MODULE_NAME app
ENV APP_MODULE app:app

COPY ./src /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
