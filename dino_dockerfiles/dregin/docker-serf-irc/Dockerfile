# Build Docker Image
FROM angelrr7702/ubuntu-13.10

MAINTAINER Bernard McKeever dregin@gmail.com

# Weechat
#RUN apt-get install -y python2.7 weechat-curses
# Weechat runs as root. Quakenet does not like this. Freenode does. Bad idea, but it's only a POC...
#ADD weechat-runner.sh /var/tmp/weechat-runner.sh
#RUN chmod +x /var/tmp/weechat-runner.sh
#ADD weechat-serf.py /.weechat/python/autoload/weechat-serf.py

# IRC-It (ii) - http://tools.suckless.org/ii/
RUN apt-get install -y ii
ADD ii-runner.sh /var/tmp/ii-runner.sh
ADD ii-controller.py /var/tmp/ii-controller.py

# Serf
RUN apt-get install -y wget unzip
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/serf/0.3.0_linux_amd64.zip -P /var/tmp/
RUN unzip /var/tmp/0.3.0_linux_amd64.zip -d /usr/bin/
ADD serf-handler.sh /var/tmp/serf-handler.sh
ADD serf-join.sh /var/tmp/serf-join.sh
EXPOSE 1337

# Supervisor
RUN apt-get install -y supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Make all scripts in /var/tmp/ executable
RUN chmod +x /var/tmp/*

CMD ["/usr/bin/supervisord"]
