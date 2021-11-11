from ubuntu:17.10
MAINTAINER Li YaLei <caidaoli@gmail.com>
# 替换阿里云源
#ADD ./sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y libssl-dev libevent-dev  unixodbc uuid-dev libssl-dev openssl curl libcurl3 libcurl3-dev
#freetds-bin freetds-dev tdsodbc
#RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
#ADD zshrc /root/.zshrc
#ADD odbc.ini /etc/odbc.ini
#ADD odbcinst.ini /etc/odbcinst.ini
#ADD freetds.conf /etc/freetds/freetds.conf
#RUN wget http://dev.mysql.com/get/DownloADDs/Connector-ODBC/5.3/mysql-connector-odbc-5.3.6-linux-ubuntu15.10-x86-64bit.tar.gz
ADD mysql-connector-odbc-5.3.6-linux-ubuntu15.10-x86-64bit.tar.gz /
# RUN tar xvzf mysql-connector-odbc-5.3.6-linux-ubuntu15.10-x86-64bit.tar.gz -C /
RUN cp /mysql-connector-odbc-5.3.6-linux-ubuntu15.10-x86-64bit/lib/* /usr/lib/odbc
 #RUN /mysql-connector-odbc-5.3.6-linux-ubuntu15.10-x86-64bit/bin/myodbc-installer
#RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
EXPOSE 5555:5555

VOLUME ["/app"]
workdir "/app"
#ENTRYPOINT ["zsh"]
