FROM jenkins
# install fontforge and ttfautohint for fonttype generation
USER root
RUN apt-get update && apt-get install -y fontforge ttfautohint bzip2
sed -i -e 's/jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024/jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 512/' /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security
USER jenkins
COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt