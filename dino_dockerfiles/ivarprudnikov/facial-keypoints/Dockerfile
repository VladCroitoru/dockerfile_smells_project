FROM python:3.6.5

RUN mkdir -p /usr/src/www

ADD . /usr/src/www/

WORKDIR /usr/src/www/app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "/usr/local/bin/gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "api:app" ]