FROM openjdk:8-jdk-alpine

ENV LANG ja_JP.UTF-8

# setup build workspace info
ENV WORKDIR /workspace
VOLUME      ${WORKDIR}
WORKDIR     ${WORKDIR}
EXPOSE      4000
ENTRYPOINT  ["run-gitbook.sh"]
CMD         ["serve"]

# install ja-font, nodejs, graphviz
COPY font/local.conf /etc/fonts/
COPY font/ipag.ttc   /usr/share/fonts/
ENV FONTCONFIG_VERSION 2.12.1-r0
ENV GRAPHVIZ_VERSION   2.38.0-r6
ENV NODE_VERSION       6.9.5-r0
RUN apk add --no-cache fontconfig=${FONTCONFIG_VERSION} \
                       graphviz=${GRAPHVIZ_VERSION} \
                       nodejs=${NODE_VERSION} && \
    fc-cache -fv

# install gitbook, plantuml
ENV GITBOOK_VERSION            3.2.2
ENV GITBOOK_CLI_VERSION        2.3.0
RUN npm install -g gitbook-cli@${GITBOOK_CLI_VERSION} && \
    gitbook fetch ${GITBOOK_VERSION}

# copy shell script
COPY bin/run-gitbook.sh /usr/bin/

# prepare GitBook directory
RUN mkdir /.gitbook && chmod 777 /.gitbook && mkdir /.npm && chmod 777 /.npm
