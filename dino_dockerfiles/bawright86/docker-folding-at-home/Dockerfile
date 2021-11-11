# Folding@home
#
# VERSION               0.1
# Run with: docker run -d -t -i magglass1/docker-folding-at-home

FROM centos:latest

# Install updates
RUN yum update -y

# Install Folding@home
RUN rpm -i https://folding.stanford.edu/releases/public/release/fahclient/centos-5.3-64bit/v7.4/fahclient-7.4.4-1.x86_64.rpm
ADD config.xml /etc/fahclient/
RUN chown fahclient:root /etc/fahclient/config.xml

CMD /etc/init.d/FAHClient start && tail -F /var/lib/fahclient/log.txt
