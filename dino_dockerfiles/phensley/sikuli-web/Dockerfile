
FROM dockerfile/java:oracle-java8
MAINTAINER "Patrick Hensley <spaceboy@indirect.com>"

ENV GRADLE gradle-2.2.1
ENV GRADLE_URL https://downloads.gradle.org/distributions/${GRADLE}-bin.zip

RUN curl -o ${GRADLE}.zip ${GRADLE_URL}
RUN unzip ${GRADLE}.zip ; rm ${GRADLE}.zip

ENV GRADLE_CMD /data/${GRADLE}/bin/gradle

COPY . /data/sikuli-web
RUN cd /data/sikuli-web ; \
    ${GRADLE_CMD} distZip

RUN cd /data/sikuli-web ; \
    VER=$(sed -nr 's/version=(.+)$/\1/p' gradle.properties) ; \
    mv build/distributions/sikuli-web-${VER}.zip /data ; \
    cd /data ; \
    rm -rf sikuli-web ${GRADLE} /root/.gradle ; \
    unzip sikuli-web-${VER}.zip ; \
    rm sikuli-web-${VER}.zip ; \
    mv sikuli-web-${VER} sikuli-web

RUN useradd sikuli && echo "sikuli:sikuli" | chpasswd && adduser sikuli sudo
RUN chown -R sikuli:sikuli /data

USER sikuli
EXPOSE 8080
CMD ["/data/sikuli-web/bin/sikuli-web", "server"]

