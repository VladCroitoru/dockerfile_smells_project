FROM debian

RUN apt-get update && \
	apt-get install -y apache2 && \
	apt-get clean
ADD run_apache.sh /
RUN chmod +x run_apache.sh
CMD ["/bin/bash", "/run_apache.sh"]

EXPOSE 80
