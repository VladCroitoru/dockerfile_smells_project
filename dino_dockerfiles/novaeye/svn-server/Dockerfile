# Alpine Linux with s6 service management
FROM smebberson/alpine-base:3.2.0

ENV SVN_URI_PREFIX=svn

	# Install Apache2 and other stuff needed to access svn via WebDav
	# Install svn
	# Installing utilities for SVNADMIN frontend
	# Create required folders
	# Create the authentication file for http access
RUN apk add --no-cache apache2 apache2-utils apache2-ldap apache2-webdav mod_dav_svn subversion &&\
	mkdir -p /run/apache2/ &&\
	mkdir /home/svn/ &&\
	mkdir -p /var/log/apache2 &&\
	mkdir /etc/subversion &&\
	touch /etc/subversion/passwd

# Add services configurations
ADD apache/ /etc/services.d/apache/

COPY subversion.conf.template /etc/apache2/conf.d/dav_svn.conf.template

VOLUME /home/svn

# Expose ports for http access
EXPOSE 80 443
