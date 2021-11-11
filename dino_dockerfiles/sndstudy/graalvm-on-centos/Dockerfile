# どのイメージを使うか
FROM centos:latest

RUN curl -sSL https://github.com/oracle/graal/releases/download/vm-1.0.0-rc1/graalvm-ce-1.0.0-rc1-linux-amd64.tar.gz > graalvm-ce-1.0.0-rc1-linux-amd64.tar.gz
RUN tar zxf graalvm-ce-1.0.0-rc1-linux-amd64.tar.gz \
    && rm graalvm-ce-1.0.0-rc1-linux-amd64.tar.gz \
    && mv graalvm-1.0.0-rc1 /var/lib/ \
    && export GRAALVM_HOME=/var/lib/graalvm-1.0.0-rc1 \
    && export JAVA_HOME=$GRAALVM_HOME \
    && export PATH=$GRAALVM_HOME/bin:$PATH

# 作成者
LABEL maintainer="sndstudy <sanada2054tech@gmail.com>"