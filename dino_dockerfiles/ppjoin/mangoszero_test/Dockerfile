FROM phusion/baseimage
RUN apt-get update && apt-get install -y libssl1.0.0 libmysql++-dev
# 设置环境变量.
ENV APP_NAME=mangoszero_test \
    MYSQL_ADDRESS=172.17.0.3 \
    MYSQL_PORT=3306 \
    MYSQL_USER=wow60 \
    MYSQL_PASSWD=12345678 \
    MYSQL_REALMD_DBNAME=wow60_realmd \
    MYSQL_WORLD_DBNAME=wow60_mangos \
    MYSQL_CHARACTER_DBNAME=wow60_character
EXPOSE 3724 8085
ENTRYPOINT ["/sbin/my_init"]
RUN rm -rf /etc/service/* && mkdir /etc/service/mangoszero
COPY startapp.sh /etc/service/mangoszero/run
RUN chmod +x /etc/service/mangoszero/run
ADD mangoszero_ubuntu16_64bit.tar.bz2 /etc/service/mangoszero/
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
