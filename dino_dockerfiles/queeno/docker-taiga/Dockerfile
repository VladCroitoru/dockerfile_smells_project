FROM python:3.5
MAINTAINER Simon Aquino "simonaquino@gmail.com"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LC_TYPE en_US.UTF-8
ENV API_NAME localhost:8000
ENV API_SCHEMA http

COPY TAIGA_VERSION /TAIGA_VERSION

RUN echo "LANG=en_US.UTF-8" > /etc/default/locale \
    && echo "LC_TYPE=en_US.UTF-8" > /etc/default/locale \
    && echo "LC_MESSAGES=POSIX" >> /etc/default/locale \
    && echo "LANGUAGE=en" >> /etc/default/locale

RUN apt-get update \
    && apt-get install -y git locales

RUN git clone -b $(cat /TAIGA_VERSION) --single-branch https://github.com/taigaio/taiga-back.git /taiga-back
RUN git clone -b $(cat /TAIGA_VERSION) --single-branch https://github.com/taigaio/taiga-front-dist /taiga-front-dist

RUN sed -i 's/^enum34/#enum34/' /taiga-back/requirements.txt \
    && sed -i -e '/sample_data/s/^/#/' /taiga-back/regenerate.sh \
    && sed -i -e '/dropdb/s/^/#/' /taiga-back/regenerate.sh \
    && sed -i -e '/createdb/s/^/#/' /taiga-back/regenerate.sh

COPY assets/config/docker-settings.py /taiga-back/settings/local.py
COPY assets/config/locale.gen /etc/locale.gen
COPY assets/config/conf.json /taiga-front-dist/dist/js/conf.json

RUN locale-gen en_US.UTF-8 \
    && dpkg-reconfigure locales \
    && locale -a

RUN pip install -r /taiga-back/requirements.txt

RUN cd /taiga-back \
    && python manage.py collectstatic --noinput

VOLUME ["/taiga-front-dist","/taiga-back/static","/taiga-back/media"]

EXPOSE 8000

WORKDIR /taiga-back

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
