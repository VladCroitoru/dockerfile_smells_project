FROM node:4

RUN apt update && apt upgrade -y && \
	cd /root && \
	git clone https://github.com/Freeboard/freeboard.git && \
	cd freeboard && \
	npm install && \
	npm install -g grunt grunt-cli 

EXPOSE 8080

WORKDIR "/root/freeboard"

CMD ["/bin/bash", "-c", "/usr/bin/python -m SimpleHTTPServer 8080"]
