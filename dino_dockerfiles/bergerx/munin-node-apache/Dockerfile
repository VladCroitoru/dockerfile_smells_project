From ubuntu:14.04

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    munin-common munin-node munin-plugins-extra munin apache2 supervisor curl && \
  apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# munin
COPY munin-node.sh /usr/local/bin/munin-node.sh
RUN sed -ri \
        -e 's/^log_file.*/# \0/' \
        -e 's/^pid_file.*/# \0/' \
        -e 's/^background 1$/background 0/' \
        -e 's/^setsid 1$/setsid 0/' \
      /etc/munin/munin-node.conf && \
    /bin/echo -e "cidr_allow 192.168.0.0/16\ncidr_allow 172.16.0.0/12\ncidr_allow 10.0.0.0/8" >> /etc/munin/munin-node.conf && \
    install -m 0755 -o munin -g munin -d /var/run/munin
ENV MUNIN_PORT=4949
ENV ALLOW=

# apache
COPY ports.conf /etc/apache2/ports.conf
COPY apache-munin.conf /etc/apache2/sites-enabled/000-default.conf
ENV MUNIN_APACHE_PORT=80

# slack
COPY slack.conf /etc/munin/munin-conf.d/slack.conf
COPY notify_slack_munin /usr/local/bin/notify_slack_munin
ENV SLACK_WEBHOOK_URL=
ENV SLACK_CHANNEL="#munin"
ENV SLACK_USERNAME="munin"
ENV SLACK_ICON_EMOJI=":munin:"

# supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

