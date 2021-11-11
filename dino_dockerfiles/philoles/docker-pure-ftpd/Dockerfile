FROM stilliard/pure-ftpd:hardened

#ENV USER ftpuser
#ENV PASSWORD qwerty
#ENV FTP_PATH /srv/ftp/
#ENV PUBLICHOST localhost

CMD echo "$PASSWORD\n$PASSWORD" | pure-pw useradd $USER -m -u ftpuser -d $FTP_PATH && /usr/sbin/pure-ftpd -c 50 -C 10 -l puredb:/etc/pure-ftpd/pureftpd.pdb -E -j -R -P $PUBLICHOST -p 30000:30009

#docker run -d --name FTP -p 21:21 -p 30000-30009:30000-30009 \
#-v /some/path/to/share:/srv/ftp -e USER=ftpuser1 -e PASSWORD=qaz123 stilliard/pure-ftpd
