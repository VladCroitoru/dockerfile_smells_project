FROM quay.io/evryfs/base-ubuntu:focal-20200916
ENV HELM_VERSION=v3.3.3
COPY test.sh /
RUN apt update && \
	apt install -y git && \
	wget -qO- https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar xzv --strip-components=1 -C /usr/local/bin/ && \
	helm plugin install --version master https://github.com/sonatype-nexus-community/helm-nexus-push.git && \
	apt-get -y clean
COPY push_charts.sh /usr/local/bin/
CMD ["/test.sh"]
