FROM roninkenji/slackware-full
MAINTAINER roninkenji

WORKDIR /tmp
COPY mysbopkg.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/mysbopkg.sh
RUN mkdir -p /srv/sbopkg/repo/SBo/14.1 /srv/sbopkg/queue /srv/sbopkg/build /srv/sbopkg/output /srv/sbopkg/src

RUN wget -nv https://github.com/sbopkg/sbopkg/releases/download/0.37.0/sbopkg-0.37.0-noarch-1_cng.tgz && installpkg sbopkg-0.37.0-noarch-1_cng.tgz
RUN gpg --quiet --fetch-key http://www.slackbuilds.org/GPG-KEY

ENTRYPOINT /usr/local/bin/mysbopkg.sh

