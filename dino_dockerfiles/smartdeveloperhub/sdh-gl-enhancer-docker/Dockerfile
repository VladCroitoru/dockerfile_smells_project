FROM alejandrofcarrera/phusion.python
MAINTAINER Alejandro F. Carrera

ENV HOME /usr/lib/glenhancer

# Create directories & virtual env
RUN virtualenv $HOME/.env
WORKDIR /usr/lib/glenhancer

# Configure runit
ADD ./my_init.d/ /etc/my_init.d/
ONBUILD ./my_init.d/ /etc/my_init.d/

CMD ["/sbin/my_init"]

# Configure volume
VOLUME ["/usr/lib/glenhancer"]

EXPOSE 5000
