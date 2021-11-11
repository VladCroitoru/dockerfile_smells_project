FROM python:3.5-alpine

ENV APP_EXPOSED_PORT 9131
ENV APP_NAME fake_ubersmith
ENV APP_ROOT /opt/$APP_NAME

EXPOSE $APP_EXPOSED_PORT

RUN apk add --no-cache --update \
    git \
    curl \
    py-pip

COPY requirements.txt $APP_ROOT/
COPY setup.py $APP_ROOT/
COPY setup.cfg $APP_ROOT/
COPY README.md $APP_ROOT/
COPY $APP_NAME $APP_ROOT/$APP_NAME

WORKDIR $APP_ROOT
RUN git init

RUN pip install -r requirements.txt && python setup.py install

HEALTHCHECK --interval=5s CMD curl -X GET --fail http://localhost:$APP_EXPOSED_PORT/status

CMD fake-ubersmith
