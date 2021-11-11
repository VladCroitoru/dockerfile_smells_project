FROM haproxy:1.6.4
RUN apt-get update -y && apt-get install -y python-pip && apt-get clean -y
RUN pip install requests supervisor supervisor-stdout
RUN mkdir -p /etc/newrelic
# Supervisord configuration
RUN mkdir -p /etc/supervisord/conf.d
COPY ./supervisord.conf /etc/supervisord.conf
CMD ["/usr/local/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
