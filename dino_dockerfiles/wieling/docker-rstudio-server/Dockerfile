FROM ubuntu:14.04
MAINTAINER Martijn Wieling <wieling@gmail.com>
RUN echo 'deb http://cran.rstudio.com/bin/linux/ubuntu trusty/' >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
RUN apt-get -qqy update
RUN apt-get install -y -q r-base=3.1.1-1trusty0 r-base-dev=3.1.1-1trusty0 gdebi-core libapparmor1 supervisor wget libcurl4-gnutls-dev
RUN (wget http://download2.rstudio.org/rstudio-server-0.98.1062-amd64.deb && gdebi -n rstudio-server-0.98.1062-amd64.deb)
RUN rm /rstudio-server-0.98.1062-amd64.deb
RUN (adduser --disabled-password --gecos "" guest && echo "guest:guest"|chpasswd)
RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 8787
CMD ["/usr/bin/supervisord"]
