FROM ubuntu:trusty
MAINTAINER witrdotnet <witr.net@gmail.com>

# Install LAMP
RUN apt-get update && \
    apt-get -yq install lamp-server^ \
    php5-gd

# Add image configuration and scripts
ADD run.sh /run.sh
RUN chmod 755 /*.sh

CMD ["/run.sh"]
