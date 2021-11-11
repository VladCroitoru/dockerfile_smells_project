FROM docker.elastic.co/logstash/logstash-oss:6.1.0

RUN logstash-plugin install logstash-output-jdbc && \
	mkdir -p /usr/share/logstash/vendor/jar/jdbc && \
	cd /usr/share/logstash/vendor/jar/jdbc && \
	curl -O https://jdbc.postgresql.org/download/postgresql-42.1.4.jar 


