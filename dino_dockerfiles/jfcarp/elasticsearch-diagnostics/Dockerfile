FROM openjdk:8
WORKDIR /tmp/
ADD https://github.com/elastic/elasticsearch-support-diagnostics/releases/download/5.11/support-diagnostics-5.11-dist.zip /tmp/
RUN unzip /tmp/support-diagnostics-5.11-dist.zip 
EXPOSE 9200
WORKDIR /tmp/support-diagnostics-5.11
ENTRYPOINT ["/tmp/support-diagnostics-5.11/diagnostics.sh"]
