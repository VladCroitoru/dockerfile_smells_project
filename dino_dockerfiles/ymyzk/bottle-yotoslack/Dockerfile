FROM python:slim
MAINTAINER Yusuke Miyazaki <miyazaki.dev@gmail.com>

COPY . /app/
WORKDIR /app/

RUN pip install -U pip setuptools wheel \
        && pip install -r requirements.txt \
        && rm -rf /root/.cache

EXPOSE 8080
ENTRYPOINT ["./app.py"]
