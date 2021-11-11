# Run with: docker run -d -t -i funnybirdboy/docker-folding-at-home

FROM ubuntu

# Install updates
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install wget -y
# Install Folding@home
RUN  wget --no-check-certificate https://fah.stanford.edu/file-releases/public/release/fahclient/debian-testing-64bit/v7.4/fahclient_7.4.4_amd64.deb
RUN dpkg -i --force-depends fahclient_7.4.4_amd64.deb
ADD config.xml /etc/fahclient/
RUN chown fahclient:root /etc/fahclient/config.xml

CMD /etc/init.d/FAHClient start && tail -F /var/lib/fahclient/log.txt
