FROM napolitano/docker-centos7-jre8

MAINTAINER Axel Napolitano <docker.2015@skjt.de>

ENV UPSOURCE_VERSION 2.0.3554

VOLUME ["/var/lib/upsource"]

RUN yum -y install tar wget && \
	yum -y install tar unzip && \
	wget -nv http://download.jetbrains.com/upsource/upsource-$UPSOURCE_VERSION.zip && \
	echo "04248791720e49d0ade4397cd45eca7cd5b1ce09f32e195583ba99e9aa0be70d *upsource-2.0.3554.zip" >> SHA256SUM && \
	sha256sum -c SHA256SUM && \
	unzip upsource-$UPSOURCE_VERSION.zip && \
	rm -f upsource-$UPSOURCE_VERSION.zip && \
	yum -y remove unzip && \
	yum -y remove wget

EXPOSE 8080

CMD ["Upsource/bin/upsource.sh", "run"]
