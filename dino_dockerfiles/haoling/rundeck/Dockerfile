FROM jordan/rundeck:latest

ADD opt/run /opt/run

RUN apt-get update &&\
    apt-get install -y vim less locales task-japanese unzip &&\
    apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

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

RUN curl -LO https://bootstrap.pypa.io/get-pip.py &&\
    python get-pip.py &&\
    pip install --upgrade pip &&\
    pip install requests websocket websocket-client python-dateutil pyyaml kubernetes

ENV TZ=Asia/Tokyo
ENV LANG=ja_JP.UTF-8
