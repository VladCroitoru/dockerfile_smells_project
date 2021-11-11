FROM smatochkin/logstash:latest

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

# Install Kibana content
RUN curl -Ls https://download.elastic.co/kibana/kibana/kibana-4.0.2-linux-x86.tar.gz | \
    tar xz -C /opt && \
    ln -s kibana-4.0.2 /opt/kibana

# Upload Kibana configuration and startup files
ADD service /etc/service
ADD https://raw.githubusercontent.com/elasticsearch/kibana/v3.1.1/sample/nginx.conf /etc/nginx/sites-available/default
RUN sed -i -e 's%root.*%root /opt/kibana;%' /etc/nginx/sites-available/default && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    sed -i -e 's%"http://"+window.location.hostname+":9200"%""%' /opt/kibana/config.js
ADD https://gist.githubusercontent.com/breyten/9579c21341c7ff2fcd42/raw/939c173aa63922c20b824c06e921c8cbb35626b5/elasticsearch.yml /opt/elasticsearch/config/elasticsearch.yml

# Expose communication ports
EXPOSE 80
EXPOSE 9200
