FROM python:3

LABEL maintainer="a.chaussier@infopen.pro"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

VOLUME /mnt

WORKDIR /mnt

ENTRYPOINT ["tox"]
