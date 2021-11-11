FROM centos:7

MAINTAINER koduki

ENV GRAALVM_URL=https://github.com/oracle/graal/releases/download/vm-1.0.0-rc1/graalvm-ce-1.0.0-rc1-linux-amd64.tar.gz \
    GRAALVM_PKG=graalvm-ce-1.0.0-rc1-linux-amd64.tar.gz \
    GRAALVM_HOME=/usr/graalvm-1.0.0-rc1

ENV LANG=en_US.UTF-8 \
    JAVA_HOME=${GRAALVM_HOME} \
    LLVM_HOME=/opt/llvm-3.9.0 \
    PATH=${LLVM_HOME}/bin:${GRAALVM_HOME}/bin:$PATH

RUN curl -L -o $GRAALVM_PKG $GRAALVM_URL &&  \
    tar xfvz $GRAALVM_PKG -C /usr/ &&  \
    rm $GRAALVM_PKG

ADD alonid-llvm-3.9.0.repo /etc/yum.repos.d/alonid-llvm-3.9.0.repo
RUN yum -y install gcc openssl-devel clang-3.9.0-devel llvm-3.9.0-devel && rm -rf /var/cache/yum && \
    alternatives --install /usr/bin/java  java  $JAVA_HOME/bin/java  20000 && \
    alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 20000 && \
    alternatives --install /usr/bin/jar   jar   $JAVA_HOME/bin/jar   20000

RUN gu -c install org.graalvm.ruby && gem install bundler
RUN gu -c install org.graalvm.r
RUN gu -c install org.graalvm.python

WORKDIR /src

CMD ["java", "-version"]