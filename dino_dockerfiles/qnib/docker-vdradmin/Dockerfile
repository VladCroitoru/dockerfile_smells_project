FROM qnib/u-terminal

RUN apt-get update && \
    apt-get install -y vdradmin-am
RUN apt-get install -y telnet
ADD var/lib/vdradmin-am/vdradmind.conf /var/lib/vdradmin-am/
RUN mkdir -p /var/run/vdradmin-am
ADD etc/supervisord.d/vdradmin.ini /etc/supervisord.d/
ADD etc/consul.d/vdradmin.json /etc/consul.d/
ADD etc/default/locale /etc/default/locale
