FROM eboraas/apache
MAINTAINER yannxia <me.yan.xia@qq.com>

RUN apt-get update && apt-get -y install php5 php5-mysql php5-gd unzip && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN /usr/sbin/a2dismod 'mpm_*' && /usr/sbin/a2enmod mpm_prefork

ADD http://bbs.startbbs.com/uploads/versions/startbbs_v1.2.3.zip /var/www/startbbs/
ADD startbbs.conf /etc/apache2/sites-enabled/
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN cd /var/www/startbbs && unzip startbbs_v1.2.3.zip && rm startbbs_v1.2.3.zip
RUN chown -R www-data /var/www/startbbs/

EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
