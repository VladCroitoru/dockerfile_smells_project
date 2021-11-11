FROM devdb/kibana
ADD assets/kibana.settings /tmp/kibana.settings
RUN /sbin/my_init& apt-get update && \ 
    apt-get install -y nodejs npm && \ 
    ln -s /usr/bin/nodejs /usr/bin/node && \ 
    npm install elasticdump -g &&  \
    ps aux && \
    curl -X POST http://localhost:9200/metsuri/logs -d "{\"sender\":\"metsuri\",\"action\":\"init\",\"date\":\"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\"}" && \
    elasticdump --output http://localhost:9200/.kibana --input /tmp/kibana.settings && \
    sleep 20
