FROM buildpack-deps:jessie-curl

RUN true && \
    echo 'deb http://jenkins.grml.org/debian jenkins-debian-glue main' >/etc/apt/sources.list.d/jdg.list && \
    curl 'http://jenkins.grml.org/debian/C525F56752D4A654.asc' | apt-key add - && \
	apt-get update && apt-get install -y --no-install-recommends \
		git \
        jenkins-debian-glue \
		jenkins-debian-glue-buildenv \
		openssh-client \
		procps \
	&& rm -rf /var/lib/apt/lists/*
