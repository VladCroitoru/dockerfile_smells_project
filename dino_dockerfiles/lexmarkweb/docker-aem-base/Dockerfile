# DOCKER-VERSION 1.0.1
FROM java:8

MAINTAINER mikemarr

ENV http_proxy=${HTTP_PROXY}
RUN apt-get update && apt-get install netcat -y

# Install utility for AEM
ADD aemInstaller.sh /aem/aemInstaller.sh
RUN chmod +x /aem/aemInstaller.sh
