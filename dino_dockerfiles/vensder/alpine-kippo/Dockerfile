FROM alpine

MAINTAINER Vensder vensder@gmail.com

RUN apk --update add \
	python \
	py-twisted \
	py-zope-interface \
	py-pip \
	subversion && \
pip install pyasn1 && \
adduser -D -s /bin/sh kippo kippo && \
cd /home && \
svn checkout http://kippo.googlecode.com/svn/trunk/ ./kippo && \
apk del --purge subversion && \
cd /home/kippo && \
mv kippo.cfg.dist kippo.cfg && \
rm -rf /home/kippo/.svn /home/kippo/.subversion && \
chown -R kippo:kippo /home/kippo && \
rm -f /var/cache/apk/*

ENV HOME /home/kippo

EXPOSE 2222
USER kippo
WORKDIR /home/kippo
CMD ["twistd", "--nodaemon", "-y", "kippo.tac", "--pidfile=kippo.pid"]
