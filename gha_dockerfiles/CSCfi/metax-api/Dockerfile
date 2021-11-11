FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /var/log/metax-api/errors && touch /var/log/metax-api/metax-api.json.log

RUN apt-get update && apt install xqilla libxerces-c-dev build-essential libssl-dev libffi-dev python-dev libxqilla-dev -y

RUN pip install --upgrade pip wheel
COPY requirements.txt /code/
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 8008
EXPOSE 8006

CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]
