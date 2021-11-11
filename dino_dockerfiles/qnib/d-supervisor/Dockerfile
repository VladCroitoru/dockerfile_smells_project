FROM debian:8.9
MAINTAINER "Christian Kniep <christian@qnib.org>"

RUN echo "2015-10-27.1";apt-get update && \
     apt-get install -y supervisor procps && \
     echo "supervisord -c /etc/supervisord.conf" >> /root/.bash_history && \
     echo "supervisorctl status" >> /root/.bash_history && \
     echo "tail -f /var/log/supervisor/" >> /root/.bash_history 
ADD etc/supervisord.conf /etc/supervisord.conf
ADD opt/qnib/supervisor/bin/start.sh /opt/qnib/supervisor/bin/
CMD ["/opt/qnib/supervisor/bin/start.sh", "-n"]

