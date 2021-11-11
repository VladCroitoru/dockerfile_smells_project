FROM topiaruss/alpine-base

MAINTAINER Gordoon Chiam <gordon.chiam@gmail.com>


ENV JDK=jdk1.8.0_66 \
    JAVA_HOME=/opt/jdk

# That's an 1.8.0_66 JDK from https://jdk8.java.net/download.html
#
# Courtesy to https://github.com/rhuss/docker-java-jolokia/blob/master/base/alpine/jre/8/Dockerfile
RUN apk add --update wget ca-certificates && \
    cd /tmp && \
    wget "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk" \
         "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-bin-2.21-r2.apk" && \
    apk add --allow-untrusted \
        glibc-2.21-r2.apk \
        glibc-bin-2.21-r2.apk && \
    /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf && \
    mkdir /opt && \
    wget http://www.java.net/download/jdk8u66/archive/b02/binaries/jdk-8u66-ea-bin-b02-linux-x64-28_jul_2015.tar.gz -O /tmp/${JDK}.tgz && \
    cd /opt && tar zxvf /tmp/${JDK}.tgz && \
    ln -s /opt/${JDK} ${JAVA_HOME} && \
    ln -s ${JAVA_HOME}/bin/java /usr/bin/java && \
    apk del wget ca-certificates && \
    rm /tmp/* /var/cache/apk/*

CMD ["/usr/bin/java", "-version"]
