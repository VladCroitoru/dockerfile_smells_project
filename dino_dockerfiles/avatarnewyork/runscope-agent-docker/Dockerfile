FROM debian:wheezy

RUN apt-get update && apt-get install wget unzip -y

ADD radar.conf.example /etc/runscope-radar/radar.conf
ADD run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh

RUN wget http://s3.amazonaws.com/runscope-downloads/runscope-radar/latest/linux-amd64/runscope-radar.zip && \
    unzip runscope-radar.zip -d /usr/local/bin/ && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* runscope-radar.zip

CMD ["/usr/local/bin/run.sh"]
