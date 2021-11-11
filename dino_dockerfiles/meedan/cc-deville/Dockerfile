# 
FROM meedan/nodejs
MAINTAINER sysops@meedan.com

ENV IMAGE=meedan/cc-deville \
    DEPLOYUSER=cc \
    DEPLOYDIR=/opt/cc \
    GITREPO=https://github.com/meedan/cc-deville.git

RUN useradd $DEPLOYUSER -s /bin/bash -m \
    && mkdir -p $DEPLOYDIR
COPY . $DEPLOYDIR
RUN chown -R ${DEPLOYUSER}:${DEPLOYUSER} ${DEPLOYDIR}

USER $DEPLOYUSER
WORKDIR $DEPLOYDIR
RUN npm install

EXPOSE 8080
CMD ["/opt/cc/start.sh"]