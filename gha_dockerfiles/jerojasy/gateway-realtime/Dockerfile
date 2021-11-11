FROM python:3.8.3-alpine

WORKDIR /src

ENV FLASK_APP index.py
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn","index:app","-b","0.0.0.0:8011","--log-level=debug","--workers","2", "--reload"]
