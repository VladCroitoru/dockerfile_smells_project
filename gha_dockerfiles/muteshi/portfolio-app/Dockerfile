FROM python:3.9-alpine3.13
LABEL maintainer="muteshi.com"

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt

# Setup directory structure
COPY ./app /app
COPY ./scripts /scripts



WORKDIR /app
EXPOSE 8000


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk update && apk add --no-cache libpq jpeg-dev && \
    apk add --update --no-cache postgresql-client && \
    apk add  --update --no-cache --virtual .build-deps \
            gcc python3-dev musl-dev postgresql-dev \
             linux-headers musl-dev zlib zlib-dev libjpeg && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .build-deps && \
    adduser --disabled-password --no-create-home user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R user:user /app && \
    chown -R user:user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER user

CMD ["run.sh"]