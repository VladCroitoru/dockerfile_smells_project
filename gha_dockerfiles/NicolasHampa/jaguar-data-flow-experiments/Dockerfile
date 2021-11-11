FROM nginx:latest

RUN rm -f /var/log/nginx/access.log && rm -f /var/log/nginx/error.log

RUN apt-get update && \
	apt-get install -y python2.7 && \
	apt-get install -y python3-numpy && \
	apt-get install -y python3-pandas && \
	apt-get install -y python3-sklearn && \
	apt-get install -y vim && \
	apt-get install -y build-essential && \
	apt-get install -y libxml2-utils && \
	apt-get install -y curl && \
	apt-get install -y git && \
    curl -L https://cpanmin.us | perl - App::cpanminus

RUN mkdir -p /var/log

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.13.0-amd64.deb && \
    dpkg -i filebeat-7.13.0-amd64.deb

COPY filebeat.yml /etc/filebeat/filebeat.yml
RUN chmod go-w /etc/filebeat/filebeat.yml

WORKDIR /PPgSI/fl-platform

RUN mkdir -p ./reports
COPY sample ./sample
COPY scripts ./scripts

RUN chmod +x scripts/coverage-comparison/*.sh
RUN chmod +x scripts/score-ranking/*.sh
RUN chmod +x scripts/utils/*.sh

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]