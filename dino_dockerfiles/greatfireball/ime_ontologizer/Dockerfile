ARG osversion=xenial
FROM ubuntu:${osversion}

ARG VERSION=master
ARG VCS_REF
ARG BUILD_DATE

RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", VERSION: "${VERSION}

LABEL maintainer="frank.foerster@ime.fraunhofer.de" \
      description="Dockerfile providing the ontologizer software" \
      version="$VERSION" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/greatfireball/ime_ontologizer"

RUN apt update && \
    apt install \
	--yes \
	--no-install-recommends \
	graphviz \
	openjdk-8-jre-headless \
	wget

WORKDIR /ontologizer

RUN wget -O Ontologizer.jar \
    http://ontologizer.de/cmdline/Ontologizer.jar

VOLUME /data
WORKDIR /data

ENTRYPOINT ["java", "-jar",  "/ontologizer/Ontologizer.jar"]
CMD ["--version"]
