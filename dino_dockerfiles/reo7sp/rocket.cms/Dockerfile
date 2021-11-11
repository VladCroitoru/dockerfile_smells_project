FROM debian:latest
MAINTAINER Oleg Morozenkov

RUN apt-get update && \
	apt-get install -y g++ cmake make binutils npm wget sed tar bash jq && \
	ln -s /usr/bin/nodejs /usr/bin/node && \
	npm install -g gulp

WORKDIR /tmp/rocketcms
COPY install-poco.sh ./
RUN sed -i 's/\r$//' install-poco.sh && bash install-poco.sh
COPY web/package.json web/
RUN cd web && npm install
COPY cpp cpp
COPY web web
COPY CMakeLists.txt ./
COPY make-build.sh ./
RUN sed -i 's/\r$//' make-build.sh && bash make-build.sh && \
	mv rocketcms /usr/local/bin/ && \
	mv *rcms.* /usr/local/lib/ && \
	mkdir -p /usr/local/share/rocketcms && \
	mv webgui /usr/local/share/rocketcms/ && \
	mv plugins /usr/local/share/rocketcms/ && \
	mv translations /usr/local/share/rocketcms/ && \
	rm -rf /tmp/rocketcms

RUN mkdir -p /var/lib/rocketcms/site
WORKDIR /var/lib/rocketcms/site
RUN /usr/local/bin/rocketcms --genconf | jq ".fs.cms.root = \"/usr/local/share/rocketcms\" | .fs.site.root = \"/var/lib/rocketcms/site\"" > rocketcms.conf.json

VOLUME /var/lib/rocketcms/site
EXPOSE 23307
CMD ["/usr/local/bin/rocketcms", "-c", "/var/lib/rocketcms/site/rocketcms.conf.json"]
