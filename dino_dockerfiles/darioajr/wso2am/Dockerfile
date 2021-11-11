FROM java:8
MAINTAINER Dario Alves Junior, darioajr@gmail.com

RUN wget -P /opt https://product-dist.wso2.com/products/api-manager/2.1.0/wso2am-2.1.0.zip && \
    apt-get update && \
    apt-get install -y zip && \
    apt-get clean && \
    unzip /opt/wso2am-2.1.0.zip -d /opt && \
    rm /opt/wso2am-2.1.0.zip

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
EXPOSE 9443
CMD ["/opt/wso2am-2.1.0/bin/wso2server.sh"]
