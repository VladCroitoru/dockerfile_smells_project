FROM qnib/d-consul

RUN apt-get update && \
    apt-get install -y dnsutils vim nmap iputils-ping procps

# dependencies needed by costum scripts (e.g. osquery)
RUN apt-get install -y python-pip libyaml-dev python-dev 
RUN /usr/bin/pip install neo4jrestclient pyyaml docopt python-consul jinja2 && \ 
    /usr/bin/pip install psutil graphitesend

# DIAMOND
RUN /usr/bin/pip install diamond
ADD etc/diamond/ /etc/diamond/
ADD opt/qnib/bin/start_diamond.sh /opt/qnib/bin/start_diamond.sh
ADD etc/supervisord.d/diamond.ini /etc/supervisord.d/diamond.ini
ADD etc/consul.d/diamond.json /etc/consul.d/

#ADD opt/qnib/bin/watch_psutil.py /opt/qnib/bin/
#ADD etc/supervisord.d/watchpsutil.ini /etc/supervisord.d/
# osqueryi
RUN cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime
