FROM hivesolutions/python:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV MONGOHQ_URL mongodb://localhost
ENV PUSHER_APP_ID PUSHER_APP_ID
ENV PUSHER_KEY PUSHER_KEY
ENV PUSHER_SECRET PUSHER_SECRET
ENV GITHUB_ID GITHUB_ID
ENV GITHUB_SECRET GITHUB_SECRET
ENV GITHUB_REDIRECT_URL GITHUB_REDIRECT_URL
ENV PYTHONPATH /src

ADD requirements.txt /
ADD extra.txt /
ADD src /src

RUN apk update && apk add libffi-dev openssl-dev
RUN pip3 install -r /requirements.txt && pip3 install -r /extra.txt && pip3 install --upgrade netius

CMD ["/usr/bin/python3", "/src/metrium/main.py"]
