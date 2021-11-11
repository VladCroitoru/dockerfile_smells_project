FROM ubuntu:20.04

MAINTAINER Alessandro Tanasi <alessandro@tanasi.it>

# Update.
RUN apt-get update

# Upgrade and install deps.
RUN set -x \ 
    && DEBIAN_FRONTEND=noninteractive apt-get install -y munin cron nginx spawn-fcgi libcgi-fast-perl \
    && apt clean && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Configure as cgi and disable localhost monitoring.
RUN set -x \ 
    && sed -i 's/^#graph_strategy cron/graph_strategy cgi/g' /etc/munin/munin.conf \
    && sed -i 's/^#html_strategy cron/html_strategy cgi/g' /etc/munin/munin.conf \
    && sed -i 's/^\[localhost\.localdomain\]/#\[localhost\.localdomain\]/g' /etc/munin/munin.conf \
    && sed -i 's/^    address 127.0.0.1/#    address 127.0.0.1/g' /etc/munin/munin.conf \
    && sed -i 's/^    use_node_name yes/#    use_node_name yes/g' /etc/munin/munin.conf

# Create munin dirs.
RUN mkdir -p /var/run/munin \
    && chown -R munin:munin /var/run/munin

COPY run.sh /usr/local/bin/start-munin
COPY nginx.conf /etc/nginx/sites-available/default

VOLUME /var/lib/munin
VOLUME /var/log/munin
VOLUME /etc/munin

EXPOSE 80
CMD ["start-munin"]
