FROM debian:8.9
MAINTAINER admin <evgeniy@kolesnyk.ru>

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install unzip screen curl -y


RUN useradd -ms /bin/bash server
RUN curl -o /home/server/ms063a6.zip http://dark-games.org.ua/files/ms/ms063a6.zip
RUN unzip /home/server/ms063a6.zip -d /home/server/
RUN rm -f /home/server/ms063a6.zip
RUN chmod +x /home/server/ms063a6/mslauncher
RUN chmod +x /home/server/ms063a6/ms.so
RUN chmod +x /home/server/ms063a6/msstats.so
RUN chmod +x /home/server/ms063a6/mswebcp.so
RUN chmod 777 /home/server/ms063a6/msstats.db


COPY restart_ms.sh /root/restart_ms.sh
RUN chmod +x /root/restart_ms.sh

EXPOSE 22 80 8888 8892 27010 27011 28906 
ENTRYPOINT /root/restart_ms.sh
