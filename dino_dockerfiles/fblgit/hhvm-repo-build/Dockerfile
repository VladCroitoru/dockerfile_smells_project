FROM phusion/baseimage:0.9.18

# Installing packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get -qy install software-properties-common wget supervisor rsync postfix mailutils unzip python-fuse libfuse2
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449
RUN add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"
RUN apt-get update
RUN apt-get -y --force-yes install hhvm
RUN apt-get clean && apt-get autoremove -yq --purge

# Scripts
ADD supervisor-config/ /etc/supervisor/conf.d/
ADD scripts/ /scripts/
RUN chmod 755 /scripts/*.sh

# Exposing HHVM-FastCGI port
EXPOSE 9000
# Exposing HHVM-FastCGI_Admin port
EXPOSE 9001

# Default command
CMD ["/scripts/start.sh"]
