FROM alpine
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Install and configure Apache WebDAV and Subversion
RUN apk --no-cache add apache2 apache2-utils apache2-webdav mod_dav_svn subversion
ADD vh-davsvn.conf /etc/apache2/conf.d/
RUN mkdir -p /run/apache2

ADD run.sh /
RUN chmod +x /run.sh
EXPOSE 80

# Define default command
CMD ["/run.sh"]
