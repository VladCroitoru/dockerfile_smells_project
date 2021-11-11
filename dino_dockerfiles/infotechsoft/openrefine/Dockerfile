# ===========================================
# infotechsoft/openrefine 
# SEE: https://github.com/OpenRefine/OpenRefine
# ===========================================

FROM infotechsoft/java:8-jre

ARG OPENREFINE_VERSION=2.8
ENV OPENREFINE_VERSION ${OPENREFINE_VERSION}
ENV OPENREFINE_PORT 3333
ENV OPENREFINE_DATA_DIR /usr/local/openrefine/data

LABEL name="infotechsoft/openrefine" \ 
	vendor="INFOTECH Soft, Inc." \
	version="${OPENREFINE_VERSION}" \
	release-date="2017-12-06" \
	maintainer="Thomas J. Taylor <thomas@infotechsoft.com>"
	

RUN yum -y install curl \
		python2 \
		unzip \
		which && \
	mkdir -p ${OPENREFINE_DATA_DIR}

ADD https://github.com/OpenRefine/OpenRefine/releases/download/${OPENREFINE_VERSION}/openrefine-linux-${OPENREFINE_VERSION}.tar.gz /usr/local/

WORKDIR /usr/local/openrefine-${OPENREFINE_VERSION}

EXPOSE ${OPENREFINE_PORT}
VOLUME ${OPENREFINE_DATA_DIR}

CMD ./refine -i 0.0.0.0 -p ${OPENREFINE_PORT} -d ${OPENREFINE_DATA_DIR}