FROM ubuntu:16.04

MAINTAINER Michael Worcester <michael.worcester@imgtec.com>


RUN apt-get update \
	&& apt-get install -y \
		git \
		ruby \
		ruby-dev \
		cmake \
		build-essential \
		bison \
		flex \
		libffi-dev \
		libxml2-dev \
		libgdk-pixbuf2.0-dev \
		libcairo2-dev \
		libpango1.0-dev \
		ttf-lyx \
		python3 \
		intltool \
		jing \
		ghostscript \
		libbatik-java \
		libavalon-framework-java \
	&& gem install --no-ri --no-rdoc asciidoctor \
	&& gem install --no-ri --no-rdoc coderay \
	&& gem install --no-ri --no-rdoc --pre asciidoctor-pdf \
	&& MATHEMATICAL_SKIP_STRDUP=1 gem install --no-ri --no-rdoc asciidoctor-mathematical \
	&& curl http://ie.archive.ubuntu.com/gnome/sources/lasem/0.5/lasem-0.5.0.tar.xz | tar -C /tmp -xJf - \
	&& cd /tmp/lasem-0.5.0 \
	&& ./configure \
	&& make \
	&& make install \
	&& ln -s /usr/local/lib/liblasem-0.6.so /usr/lib/liblasem.so \
	&& rm -rf /tmp/lasem-0.5.0

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

WORKDIR /documents
VOLUME /documents

CMD ["/bin/bash"]


