FROM python:3.9-alpine3.13
LABEL maintainer="AlternaLearn"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./Django /Django
COPY ./scripts /scripts

WORKDIR /Django
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home django && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R django:django /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER django

CMD ["run.sh"]
