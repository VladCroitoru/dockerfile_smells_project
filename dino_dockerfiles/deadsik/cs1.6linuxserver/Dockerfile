FROM debian:8.9
MAINTAINER admin <evgeniy@kolesnyk.ru>

RUN export DEBIAN_FRONTEND=noninteractive
RUN rm -f /var/lib/apt/lists/lock
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install unzip lib32gcc1 screen curl -y
RUN curl -o /root/hlds_6153_linux.zip http://dark-games.org.ua/files/hlds/hlds_6153_linux.zip
RUN mkdir -p /root/server/
RUN unzip /root/hlds_6153_linux.zip -d /root/server/
RUN rm -f /root/hlds_6153_linux.zip
RUN touch /root/server/cstrike/listip.cfg
RUN touch /root/server/cstrike/banned.cfg
RUN echo "cd /root/server/" > /root/server/start.sh
RUN echo "screen -A -m -d -S cs27015 ./hlds_run -game cstrike +ip 0.0.0.0 -autoupdate -pingboost 2 -port 27015 +maxplayers 32 +map de_dust2" >> /root/server/start.sh
RUN chmod +x /root/server/start.sh
RUN chmod +x /root/server/hlds_run
RUN chmod +x /root/server/hlds_linux

COPY start.sh /root/start.sh
RUN chmod +x /root/start.sh

EXPOSE 22 27015
ENTRYPOINT /root/start.sh
