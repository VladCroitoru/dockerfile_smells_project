FROM starlight36/httpd-subversion
MAINTAINER John Lianoglou <prometheas@github>

COPY fs/ /

# configure apache
RUN \
	echo "User www-data" >> /usr/local/apache2/conf/httpd.conf && \
	cat /usr/local/svn-wc-attendant/apache2/svn-repo.conf >> /usr/local/apache2/conf/extra/httpd-svn.conf

# prepare svn repository
RUN init_repo.sh
