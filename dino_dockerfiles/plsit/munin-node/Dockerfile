FROM ubuntu:14.04

# munin 2.0.55
RUN apt-get update -y && \
      apt-get install -y software-properties-common && \
      add-apt-repository -y ppa:pneu/munin && \
      apt-get update -y && \
      apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update -y && \
      apt-get install -y python munin-node munin-plugins-extra telnet mtr wget dnsutils && \
      apt-get clean && \
      rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN ln -s /usr/share/munin/plugins/cpu_by_process /etc/munin/plugins/cpu_by_process && mkdir -p /var/log/munin/; chown -R munin:munin /var/log/munin/

ADD ./autoconfigure.py /usr/bin/munin-node-autoconfigure
RUN chmod +x /usr/bin/munin-node-autoconfigure

ADD bootstrap.sh /root/bootstrap.sh

EXPOSE 4949

CMD /root/bootstrap.sh
