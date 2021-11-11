FROM python:3-alpine

ENV REDIS_URL 'redis://redis:6379'
ENV DJANGO_SETTINGS_MODULE 'settings'

ADD ./ /opt/otree

RUN apk -U add --no-cache postgresql-dev gcc musl-dev curl \
                          bash postgresql \
    && pip install -r /opt/otree/requirements.txt \
    && curl https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz -O \
	&& cd /usr/local/bin \
	&& tar -xf /forego-stable-linux-amd64.tgz \
	&& rm /forego-stable-linux-amd64.tgz \
    && mkdir -p /opt/init \
    && chmod +x /opt/otree/entrypoint.sh \
    && apk del postgresql-dev gcc musl-dev curl

RUN echo "oTree: /bin/bash -c 'cd /opt/otree && otree runprodserver --port=80'"> /Procfile

WORKDIR /opt/otree
VOLUME /opt/init
ENTRYPOINT /opt/otree/entrypoint.sh
EXPOSE 80
