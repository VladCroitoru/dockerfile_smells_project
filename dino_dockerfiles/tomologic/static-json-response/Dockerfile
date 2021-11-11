FROM python:3-alpine
EXPOSE 8080

# Requirements to compile greenlet and gevent
RUN apk add gcc musl-dev --no-cache

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data.json server.py ./
CMD ["/usr/src/app/server.py"]
