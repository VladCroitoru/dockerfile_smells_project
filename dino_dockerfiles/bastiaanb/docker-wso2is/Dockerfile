#
# WSO2 API Manager 1.9.0
#
FROM java:7
MAINTAINER Bastiaan Bakker, bastiaan@nakednerds.net

RUN wget -P /opt --user-agent="testuser" --referer="http://connect.wso2.com/wso2/getform/reg/new_product_download"  \
        http://product-dist.wso2.com/products/identity-server/5.0.0/wso2is-5.0.0.zip && \
    echo 7dd0cf1193ce396f66f704fca5118efd00c7fe3792a84fb3fe72e41bbc949cb8 /opt/wso2is-5.0.0.zip | sha256sum -c --quiet && \
    wget -P /opt --user-agent="testuser" --referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" \
        http://product-dist.wso2.com/products/identity-server/5.0.0/service-pack/WSO2-IS-5.0.0-SP01.zip && \
    echo 7b2e7999ad98a1d83175a91ad14e7d178feb3a6245d43b4fb286178599c0d5c0 /opt/WSO2-IS-5.0.0-SP01.zip | sha256sum -c --quiet && \
    apt-get update && \
    apt-get install -y zip ant && \
    apt-get clean && \
    unzip /opt/wso2is-5.0.0.zip -d /opt && \
    rm /opt/wso2is-5.0.0.zip && \
    unzip /opt/WSO2-IS-5.0.0-SP01.zip -d /opt && \
    rm /opt/WSO2-IS-5.0.0-SP01.zip && \
    cd /opt/WSO2-IS-5.0.0-SP01 && \
    sh ./install_sp.sh

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
EXPOSE 9443
CMD ["/opt/wso2is-5.0.0/bin/wso2server.sh"]
