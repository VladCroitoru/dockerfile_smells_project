FROM python:3.6-alpine

RUN apk update
RUN apk add rsync

COPY ./ /code
WORKDIR /code

RUN ln -s /code/backup /usr/bin/

RUN pip install -r requirements.txt

RUN echo 'uid root' >> /etc/rsyncd.conf
RUN echo 'read only = true' >> /etc/rsyncd.conf

CMD backup
