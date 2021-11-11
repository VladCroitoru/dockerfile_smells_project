#
# Graylog web interface Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV WEB_INT_VERSION graylog-web-interface-1.3.4
ENV APPLICATION_SECRET deL8KgPYbjORlwudXWrPqrGHf4HEIBWkcK7yAVC5PtUO0mrI1y6v7NTKbYsCN7Ey7NGVvEAv1SClyRGoQDbN5W1iUQgYJKXT
ENV GRAYLOG2_SERVER_URIS http://127.0.0.1:12900/,http://127.0.0.1:12910/

# Update & install packages for graylog
RUN apt-get update && \
    apt-get install -y wget openjdk-7-jre

#Install and configure web interface
RUN wget --no-check-certificate https://packages.graylog2.org/releases/graylog2-web-interface/$WEB_INT_VERSION.tgz && \
 tar xvfz $WEB_INT_VERSION.tgz
ADD graylog-web-interface.conf /$WEB_INT_VERSION/conf/

#RUN sed -i \
#    -e "s|\$APPLICATION_SECRET|$APPLICATION_SECRET|g" \
#    /$WEB_INT_VERSION/conf/graylog-web-interface.conf

#Add link for binary
RUN ln -s /$WEB_INT_VERSION/bin/graylog-web-interface /usr/bin/graylog-web-interface && ls -l /usr/bin/graylog-web-interface

EXPOSE 9000

ADD start.sh /

CMD ["/bin/bash", "/start.sh"]
