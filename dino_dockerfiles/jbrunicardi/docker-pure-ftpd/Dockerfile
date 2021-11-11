FROM stilliard/pure-ftpd
MAINTAINER jbrunicardi@gmail.com

RUN usermod -u 80 ftpuser
RUN groupmod -g 80 ftpgroup
RUN usermod -g 80 ftpuser

# startup
CMD /usr/sbin/pure-ftpd -H -l puredb:/home/ftpusers/conf/pure-ftpd/pureftpd.pdb -O w3c:/home/ftpusers/logs/pureftpd.log -E -R -P $PUBLICHOST -p 50000:50100

EXPOSE 21 50000-50100
