FROM tvial/docker-mailserver:latest
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y munin-node
RUN rm /etc/munin/plugins/*
RUN ln -s /usr/share/munin/plugins/postfix_mailqueue /etc/munin/plugins/postfix_mailqueue && \
    ln -s /usr/share/munin/plugins/postfix_mailstats /etc/munin/plugins/postfix_mailstats && \
    ln -s /usr/share/munin/plugins/postfix_mailvolume /etc/munin/plugins/postfix_mailvolume && \
    ln -s /usr/share/munin/plugins/fail2ban /etc/munin/plugins/fail2ban && \
    ln -s /usr/share/munin/plugins/amavis /etc/munin/plugins/amavis && \
    ln -s /usr/share/munin/plugins/memory /etc/munin/plugins/memory && \
    ln -s /usr/share/munin/plugins/swap /etc/munin/plugins/swap
ADD start-mailserver.sh /usr/local/bin
ADD munin-node.conf /etc/munin
