FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
	apk update && \
	apk add --no-cache --virtual .build-deps postgresql-dev gcc libc-dev make lapack-dev && \
	apk add --no-cache --virtual .run-deps lapack libpq libgomp libatomic && \
	ln -s /usr/include/locale.h /usr/include/xlocale.h && \
	pip install --no-cache-dir -r requirements.txt &&\
	apk del .build-deps

COPY . /app

CMD python3 main.py