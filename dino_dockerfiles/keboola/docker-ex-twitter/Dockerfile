# VERSION 0.0.1
FROM keboola/base-php56
MAINTAINER Ondrej Vana <ondrej.vana@keboola.com>

WORKDIR /home

# Initialize
RUN echo "memory_limit = -1" >> /etc/php.ini
RUN git clone https://github.com/keboola/generic-extractor.git ./
RUN git checkout twitter
RUN composer install --no-interaction

ENTRYPOINT php ./run.php --data=/data
