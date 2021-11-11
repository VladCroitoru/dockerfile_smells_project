FROM ruby:2.1.3
RUN apt-get update
RUN apt-get install -y postgresql-client nodejs netcat ca-certificates curl gcc libc6-dev make bzr git mercurial --no-install-recommends
RUN rm -rf /var/lib/apt/lists/*
ENV GOLANG_VERSION 1.3.3
RUN curl -sSL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz | tar -C /usr/src -xz
RUN cd /usr/src/go/src && ./make.bash --no-clean 2>&1
ENV PATH /usr/src/go/bin:$PATH
