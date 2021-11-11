FROM nginx:alpine

MAINTAINER Florian Maffini <florian.maffini@free.fr>

COPY jq1.5-linux64 /bin/jq
RUN chmod a+x /bin/jq

COPY init.sh /init.sh
RUN chmod a+x /init.sh

COPY default.conf /etc/nginx/conf.d/default.conf

ENV DATA_DIR /data
ENV SRC_FILE /data.json
ENV DST_FILENAME index.json
ENV ENDPOINTS_FILE /endpoints

CMD /bin/sh -c "/init.sh && nginx -g 'daemon off;'"