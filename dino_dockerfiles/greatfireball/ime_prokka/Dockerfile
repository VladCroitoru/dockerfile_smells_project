ARG osversion=xenial-20181005
FROM ubuntu:${osversion}

ARG VERSION=master
ARG VCS_REF
ARG BUILD_DATE

RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", VERSION: "${VERSION}

LABEL maintainer="frank.foerster@ime.fraunhofer.de" \
      description="Dockerfile providing the PROKKA annotation pipeline" \
      version=${VERSION} \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.vcs-url="https://github.com/greatfireball/ime_prokka"

WORKDIR /opt

ENV PATH=/opt/barrnap/bin/:"$PATH"

RUN apt update && \
    apt install --yes \
	build-essential \
	libdatetime-perl \
	libxml-simple-perl \
	libdigest-md5-perl \
	git \
	default-jre \
	bioperl && \
    cpan Bio::Perl && \
    git clone https://github.com/tseemann/barrnap.git /opt/barrnap && \
    cd /opt/barrnap && \
    git checkout 0.9 && \
    rm -rf .git && \
    git clone https://github.com/tseemann/prokka.git /opt/prokka && \
    cd /opt/prokka && \
    git checkout v1.13.4 && \
    rm -rf .git && \
    /opt/prokka/bin/prokka --setupdb && \
    apt --yes remove \
        git \
	build-essential && \
    apt --yes autoremove && \
    apt --yes install less && \
    apt --yes autoclean && \
    apt --yes clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH=/opt/prokka/bin/:"$PATH"

VOLUME /data
WORKDIR /data

ENTRYPOINT ["prokka"]
