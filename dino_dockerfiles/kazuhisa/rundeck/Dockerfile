FROM jordan/rundeck:2.10.6

MAINTAINER Kazuhisa Yamamoto

RUN apt-get update
RUN apt-get install -y vim less locales task-japanese unzip

RUN { \
    echo '[mysqld]'; \
    echo 'character-set-server=utf8'; \
    echo 'collation-server=utf8_general_ci'; \
    echo '[client]'; \
    echo 'default-character-set=utf8'; \
} > /etc/mysql/conf.d/charset.cnf

RUN cp -p /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN { \
    echo 'Asia/Tokyo'; \
} > /etc/timezone

RUN sed -i -e 's/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/g' /etc/locale.gen
RUN echo LANG=ja_JP.UTF-8 > /etc/locale.conf
RUN locale-gen

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "/tmp/awscli-bundle.zip"
RUN unzip /tmp/awscli-bundle.zip -d /tmp
RUN /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
