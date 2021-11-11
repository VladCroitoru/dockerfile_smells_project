FROM littleq0903/ntpc-frontdesk-env
MAINTAINER Colin Su

WORKDIR $HOME

RUN mkdir src
ADD . src

WORKDIR src

RUN bower --allow-root install

CMD python manage.py runserver 0.0.0.0:8000 --insecure

EXPOSE 8000
