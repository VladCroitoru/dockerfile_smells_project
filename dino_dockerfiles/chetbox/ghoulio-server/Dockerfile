FROM chetbox/ghoulio:2.3.4
MAINTAINER chetbox

# Insall Java
RUN apt-get update && \
    apt-get -y install openjdk-7-jre-headless && \
    apt-get clean all

# Install Leiningen
RUN mkdir -p /opt/bin && \
    wget -q https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein -O /opt/bin/lein && \
    chmod +x /opt/bin/lein
ENV LEIN_ROOT 1
ENV PATH $PATH:/opt/bin

ADD . /server
WORKDIR /server

# Build
RUN lein uberjar

ENV PORT 80
ENTRYPOINT []
CMD ["/bin/bash", "-c", "java -jar target/ghoulio-server-*-standalone.jar"]
EXPOSE 80
