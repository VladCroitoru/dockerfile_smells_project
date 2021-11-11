FROM python:3.5-slim

RUN apt-get update && apt-get install -y \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY run-gnocchi.sh /
RUN pip install -U gnocchi[file,redis,postgresql] uwsgi gnocchiclient
RUN mkdir /etc/gnocchi
RUN chmod 777 /etc/gnocchi
ADD uwsgi.ini /etc/gnocchi
EXPOSE 8041
CMD /run-gnocchi.sh
