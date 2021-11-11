FROM kibana:5.2.0

RUN kibana-plugin install https://github.com/sivasamyk/logtrail/releases/download/0.1.8/logtrail-5.2.0-0.1.8.zip

RUN mkdir /config && \
    mv /usr/share/kibana/plugins/logtrail/logtrail.json /config/logtrail.json && \
    ln -s /config/logtrail.json /usr/share/kibana/plugins/logtrail/logtrail.json

