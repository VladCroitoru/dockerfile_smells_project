FROM python:3.9-alpine

ENV PATH="/scripts:${PATH}"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev

RUN pip install --upgrade pip

RUN mkdir /app
COPY . /app
WORKDIR /app
COPY ./scripts /scripts
COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN chmod +x /scripts/*

CMD ["entrypoint.sh"]