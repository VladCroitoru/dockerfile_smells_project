FROM ubuntu:14.04
MAINTAINER Minsheng Lin <minsheng.l@inwinstack.com>

USER root

# avoid error in install package
ENV DEBIAN_FRONTEND noninteractive
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

COPY ./packages/calamari*.deb /

RUN apt-get update && apt-get install psmisc apache2 libapache2-mod-wsgi libcairo2 libpq5 postgresql python-cairo salt-master salt-minion supervisor python-sqlalchemy python-twisted python-txamqp python-greenlet python-gevent python-support python-msgpack python-six python-configobj -y && dpkg -i /*.deb && rm -f /*.deb

EXPOSE 80/tcp 2003/tcp 4505/tcp 4506/tcp

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
