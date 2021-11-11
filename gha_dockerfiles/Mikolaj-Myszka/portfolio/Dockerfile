FROM python:3.9-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp
# RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web

RUN adduser --disabled-password user
RUN chown -R user:user /vol
# RUN chmod -R 777 /vol/web
 RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
