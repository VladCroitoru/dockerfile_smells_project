# Folding@home
#
# VERSION               0.1
# Run with: docker run -d -t -i magglass1/docker-folding-at-home

FROM fedora

# Install updates
RUN yum update -y

# Install Folding@home
RUN rpm -i https://fah.stanford.edu/file-releases/public/release/fahclient/centos-5.3-64bit/v7.3/fahclient-7.3.6-1.x86_64.rpm
ADD config.xml /etc/fahclient/
RUN chown fahclient:root /etc/fahclient/config.xml

CMD /etc/init.d/FAHClient start && tail -F /var/lib/fahclient/log.txt
