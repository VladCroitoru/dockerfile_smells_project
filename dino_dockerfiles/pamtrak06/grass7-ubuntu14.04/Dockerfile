FROM pamtrak06/ubuntu14.04-apache2-python

MAINTAINER pamtrak06 <pamtrak06@gmail.com>

RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
RUN add-apt-repository -y ppa:grass/grass-stable
RUN apt-get update
RUN apt-get install -y --force-yes grass7 grass7-doc

# Expose ports
#EXPOSE 22 80 443

# Define default command
#CMD ["apachectl", "-D", "FOREGROUND"]
