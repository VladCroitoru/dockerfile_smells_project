FROM alpine:latest

RUN apk add --update python git py-pip

COPY . /opt/pocket_latest_read_articles
WORKDIR /opt/pocket_latest_read_articles
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/opt/pocket_latest_read_articles/webapp.py"]
