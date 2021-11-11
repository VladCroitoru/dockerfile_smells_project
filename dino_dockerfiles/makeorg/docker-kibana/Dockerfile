FROM kibana:5.6.3

RUN apt-get update && apt-get install patch
RUN apt-get install zip unzip

COPY ./logtrail.patch /tmp/logtrail.patch

RUN wget -qO /tmp/logtrail.zip https://github.com/sivasamyk/logtrail/releases/download/v0.1.23/logtrail-5.6.3-0.1.23.zip
RUN unzip -q /tmp/logtrail.zip -d /tmp/logtrail
RUN patch -d /tmp/ -p0 < /tmp/logtrail.patch
RUN cd /tmp/logtrail && zip -r /tmp/logtrail.zip kibana

RUN kibana-plugin install file:///tmp/logtrail.zip
RUN ln -s -f /etc/kibana/logtrail.json /usr/share/kibana/plugins/logtrail/logtrail.json
