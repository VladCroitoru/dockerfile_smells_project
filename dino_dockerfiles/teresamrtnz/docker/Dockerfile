FROM debian:jessie
MAINTAINER teresamrtnz@gmail.com
RUN apt-get update && apt-get install -y php5 libapache2-mod-php5 php5-mysql php5-cli
RUN ln -sf /dev/stdout /var/log/apache2/access.log 
RUN ln -sf /dev/stderr /var/log/apache2/error.log
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
