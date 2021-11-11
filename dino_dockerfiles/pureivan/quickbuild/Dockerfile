FROM jeanblanchard/java:jre-8u151
MAINTAINER pureivan

# set timezone
ENV  TIME_ZONE Asia/Shanghai

RUN \
apk add --no-cache tzdata;\
echo "${TIME_ZONE}" > /etc/timezone; \
ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime;

# Download and Install 
RUN \
apk add --update --no-cache curl python py-pip git subversion rsync;\
pip install supervisor;\
apk update && apk add --no-cache ca-certificates && update-ca-certificates && apk add --no-cache openssl;

# Download and Install quickbuild
WORKDIR /opt/

RUN \
curl https://www.pmease.com/quickbuild/downloads -o qbdownload.html; \
wget `cat qbdownload.html | grep "zip" | sed 's/^.*href=\"//g' | sed 's/\"><i.*$//g' | sed 's/amp\;//g' | sed 's/^/http:\/\/www.pmease.com/'` -O `cat qbdownload.html | grep "zip" | sed 's/^.*href=\"//g' | sed 's/\"><i.*$//g' | sed 's/^.*\///g'` ; \
unzip `cat qbdownload.html | grep "zip" | sed 's/^.*href=\"//g' | sed 's/\"><i.*$//g' | sed 's/^.*\///g'`;\
rm -f `cat qbdownload.html | grep "zip" | sed 's/^.*href=\"//g' | sed 's/\"><i.*$//g' | sed 's/^.*\///g'`;\
ln -s `cat qbdownload.html | grep "zip" | sed 's/^.*href=\"//g' | sed 's/\"><i.*$//g' | sed 's/^.*\///g' | sed 's/\.zip//g'` quickbuild;\
rm -f qbdownload.html;\
rm -rf /var/cache/apk/*;\
mkdir qbhome;

EXPOSE 8810
CMD /opt/quickbuild/bin/server.sh console
