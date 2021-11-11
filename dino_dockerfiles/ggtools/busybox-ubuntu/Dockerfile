# Busybox-ubuntu with curl and gosu commands

FROM busybox:ubuntu-14.04
MAINTAINER Christophe Labouisse <christophe@labouisse.org>

# Install curl with ssl support
RUN (wget -O - http://www.magicermine.com/demos/curl/curl/curl-7.30.0.ermine.tar.bz2 | bunzip2 -c - | tar xf -) \
  && mv /curl-7.30.0.ermine/curl.ermine /bin/curl \
  && rm -Rf /curl-7.30.0.ermine

# Grab gosu
RUN curl -o /bin/gosu -SkL 'https://github.com/tianon/gosu/releases/download/1.1/gosu' \
	&& chmod +x /bin/gosu

# Add a default group
RUN echo >>/etc/group "default:x:1000:"

# Add a default user
RUN echo >>/etc/passwd "default:x:1000:1000:Default non-root user:/home/default:/bin/sh"

# Create home directory for the default user
RUN mkdir -p /home/default && chown default:default /home/default

# Adjust /tmp permissions
RUN chmod 1777 /tmp

CMD ["/bin/sh"]
