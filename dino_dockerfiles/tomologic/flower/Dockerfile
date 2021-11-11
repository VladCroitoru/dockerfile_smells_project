FROM python:3.6-alpine
EXPOSE 8080

# Requirements to compile hiredis
RUN apk add gcc musl-dev --no-cache

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh /usr/src/app/
CMD ["/usr/src/app/run.sh"]
