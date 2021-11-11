# Docker container with chef-solo & berkshelf
FROM ubuntu
MAINTAINER Tom Eklöf "tom@linux-konsult.com"

ADD http://download-new.utorrent.com/endpoint/utserver/os/linux-x64-debian-6-0/track/beta/ /tmp/utorrent.tar.gz
ADD http://launchpadlibrarian.net/103002189/libssl0.9.8_0.9.8o-7ubuntu3.1_amd64.deb /tmp/

RUN dpkg -i /tmp/libssl0.9.8_0.9.8o-7ubuntu3.1_amd64.deb && cd /opt/ && tar xvzf /tmp/utorrent.tar.gz && ln -s /opt/$(ls /opt/|tail -1) /opt/utorrent-server && rm -f /tmp/utorrent.tar.gz /tmp/libssl0.9.8_0.9.8o-7ubuntu3.1_amd64.deb

# Expose the port (you also need to portmap this if you're behind a NAT router)
EXPOSE 6881

# Expose the web interface
EXPOSE 8080

CMD ["/opt/utorrent-server/utserver", "-settingspath", "/opt/utorrent-server/"]
