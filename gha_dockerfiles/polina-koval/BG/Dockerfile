FROM python:3.9-alpine

WORKDIR /BG

COPY requirements.txt requirements.txt
# Install postgres client
RUN apk add --update --no-cache postgresql-client
# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev


# Remove dependencies
RUN python3 -m pip install --upgrade pip
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && python3 -m pip install --upgrade Pillow \
    && apk del build-deps

RUN pip install -r requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:8000