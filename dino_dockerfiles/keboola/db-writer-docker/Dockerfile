#VERSION 1.0.0
FROM quay.io/keboola/docker-php56-all-db
MAINTAINER Miro Cillik <miro@keboola.com>

# Run extractor
ENV TDSVER=8.0
WORKDIR /home
RUN echo "memory_limit = -1" >> /etc/php.ini
RUN git clone https://github.com/keboola/db-writer.git ./
RUN git checkout tags/0.0.18
RUN composer install --no-interaction

ENTRYPOINT php ./run.php --data=/data
