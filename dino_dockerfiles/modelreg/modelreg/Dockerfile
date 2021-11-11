FROM python:3
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install gettext -y
COPY requirements.txt /usr/src/app/requirements.txt
RUN wget https://github.com/vhf/confusable_homoglyphs/raw/master/confusable_homoglyphs/confusables.json
RUN wget https://github.com/vhf/confusable_homoglyphs/raw/master/confusable_homoglyphs/categories.json
RUN pip install psycopg2
RUN pip install uwsgi
RUN pip install -r requirements.txt

EXPOSE 9090

ENV DJANGO_SETTINGS_MODULE=modelreg.settings_docker

CMD bash /usr/src/app/boot.sh

COPY scripts/boot.sh /usr/src/app/boot.sh
COPY manage.py /usr/src/app/

COPY locale    /usr/src/app/locale
COPY modelreg  /usr/src/app/modelreg
RUN python manage.py compilemessages
