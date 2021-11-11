FROM library/debian:jessie
RUN apt-get update && apt-get -y install apache2 libapache2-mod-php5 && apt-get clean && rm -rf /var/cache/apt /var/lib/{apt,dpkg}
RUN apt-get -y install net-tools less
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
