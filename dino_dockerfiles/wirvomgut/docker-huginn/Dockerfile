FROM cantino/huginn
MAINTAINER Julian liebl

RUN apt-get update && apt-get install -y \
    duplicity \
    ncftp \
 && rm -rf /var/lib/apt/lists/*

VOLUME /var/lib/mysql

EXPOSE 3000

CMD ["/scripts/init"]
