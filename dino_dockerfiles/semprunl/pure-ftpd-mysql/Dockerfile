FROM kauden/pure-ftpd-mysql

RUN apt-mark hold pure-ftpd pure-ftpd-common

ADD entrypoint.sh /entrypoint.sh
ADD mysql.conf /etc/pure-ftpd/db/mysql.conf

RUN chmod +x /*.sh
CMD ["/entrypoint.sh"]