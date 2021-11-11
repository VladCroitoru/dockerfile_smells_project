FROM rancher/os-debianconsole:v0.4.5

MAINTAINER Vincent Vaz <contact@sleeck.eu>

RUN apt-get install wget nfs-common -y
RUN wget $(wget -qO- https://api.github.com/repos/ContainX/docker-volume-netshare/releases/latest | grep browser_download_url |grep "amd64.deb" | head -n 1 | cut -d '"' -f 4) -O /tmp/current.deb
RUN dpkg -i /tmp/current.deb
RUN rm /tmp/current.deb
ADD console.sh /usr/sbin/console.sh
RUN chmod +x /usr/sbin/console.sh

ENTRYPOINT ["/usr/sbin/entry.sh"]
CMD ["/usr/sbin/console.sh"]