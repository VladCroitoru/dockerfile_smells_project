FROM hivesolutions/python:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV FORCE_SSL 1
ENV MONGOHQ_URL mongodb://localhost
ENV SENDER_EMAIL "Mailme <no-reply@mailme.com>"
ENV INLINER_ENGINE premailer
ENV SMTP_HOST SMTP_HOST
ENV SMTP_PORT 25
ENV SMTP_SSL 1
ENV SMTP_USER SMTP_USER
ENV SMTP_PASSWORD SMTP_PASSWORD
ENV SMTP_HELO_HOST SMTP_HELO_HOST
ENV PYTHONPATH /src

ADD requirements.txt /
ADD extra.txt /
ADD src /src

RUN apk update && apk add libxml2-dev libxslt-dev
RUN pip3 install -r /requirements.txt && pip3 install -r /extra.txt && pip3 install --upgrade netius

CMD ["/usr/bin/python3", "/src/mailme/main.py"]
