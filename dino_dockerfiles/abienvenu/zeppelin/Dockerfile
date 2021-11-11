FROM alpine

ARG DIST_MIRROR=http://archive.apache.org/dist/zeppelin
ARG VERSION=0.7.1

ENV ZEPPELIN_HOME=/opt/zeppelin \
	JAVA_HOME=/usr/lib/jvm/java-1.7-openjdk \
	PATH=$PATH:/usr/lib/jvm/java-1.7-openjdk/jre/bin:/usr/lib/jvm/java-1.7-openjdk/bin

# Base Zeppelin 
RUN apk update && apk add --upgrade bash curl ca-certificates jq openjdk7 git && \
	mkdir -p ${ZEPPELIN_HOME} && \
	curl ${DIST_MIRROR}/zeppelin-${VERSION}/zeppelin-${VERSION}-bin-all.tgz | tar xz -C ${ZEPPELIN_HOME} && \
	mv ${ZEPPELIN_HOME}/zeppelin-${VERSION}-bin-all/* ${ZEPPELIN_HOME} && \
	rm -rf ${ZEPPELIN_HOME}/zeppelin-${VERSION}-bin-all && \
	rm -rf *.tgz

# Add python2 with matplotlib, pandas, mysqldb
RUN apk add python python-dev py-pip libpng-dev freetype-dev gcc g++ gfortran py-mysqldb && \
	pip install --upgrade pip && \
	pip install py4j && \
	ln -s /usr/include/locale.h /usr/include/xlocale.h && \
	pip install matplotlib && \
	pip install pandas && \
	pip install -U pandasql && \
	rm -rf /var/cache/apk/*

EXPOSE 8080 8443
VOLUME ${ZEPPELIN_HOME}/logs \
	${ZEPPELIN_HOME}/notebook

WORKDIR ${ZEPPELIN_HOME}

CMD ./bin/zeppelin.sh run

