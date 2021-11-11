FROM qnib/u14-consul
MAINTAINER "Christian Kniep <christian@qnib.org>"

RUN apt-get install -y dnsutils vim nmap

# dependencies needed by costum scripts (e.g. osquery)
RUN apt-get install -y python-pip libyaml-dev python-dev 
RUN /usr/bin/pip install neo4jrestclient pyyaml docopt python-consul jinja2 && \ 
    /usr/bin/pip install psutil graphitesend
#ADD opt/qnib/bin/watch_psutil.py /opt/qnib/bin/
#ADD etc/supervisord.d/watchpsutil.ini /etc/supervisord.d/
# osqueryi

