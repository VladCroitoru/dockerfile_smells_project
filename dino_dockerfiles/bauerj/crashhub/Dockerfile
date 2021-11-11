FROM python:3
LABEL maintainer="Johann Bauer <bauerj@bauerj.eu>"

RUN pip install uwsgi PyMySQL
RUN useradd crashhub

COPY . /app

RUN python /app/setup.py install

USER crashhub

WORKDIR /app

CMD uwsgi --socket 0.0.0.0:3031 --processes 2 --threads 2 --master --wsgi-file /app/crashhub.py --callable app
