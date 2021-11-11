FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -yyq netcat


WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . /app/
CMD ./entrypoint.sh