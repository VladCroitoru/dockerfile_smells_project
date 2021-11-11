# building a docker page 
FROM python:3.8-slim-buster
ENV PTHONUNBUFFERED=1

WORKDIR /app_my
COPY requirements.txt  requirements.txt
# RUN apk add --update --no-cache postgresql-client jpeg-dev
# RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
#gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
# RUN apk del .tmp-build-deps
RUN pip install --no-cache-dir -r requirements.txt