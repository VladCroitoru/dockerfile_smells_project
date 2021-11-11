FROM postgres
MAINTAINER Mujtaba Al-Tameemi <mujtaba@changeheroes.com>

ENV POSTGRES_DB pagila
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD admin

COPY *.sh /docker-entrypoint-initdb.d/
COPY *.sql /docker-entrypoint-initdb.d/dump/

EXPOSE 5432
CMD ["postgres"]