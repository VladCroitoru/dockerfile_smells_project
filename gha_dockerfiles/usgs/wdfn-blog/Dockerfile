FROM debian:stretch-slim

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    curl \
    gnupg 

# Install Hugo from tar distribution to /usr/local/bin
RUN curl --silent --location https://github.com/gohugoio/hugo/releases/download/v0.61.0/hugo_0.61.0_Linux-64bit.tar.gz > hugo.tar.gz
RUN tar xzf hugo.tar.gz -C /usr/local/bin


# Install node.js 14.x (LTS at time of writing) from official package.
RUN curl --silent --location https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get -y update
RUN apt-get install -y nodejs

COPY . /src
WORKDIR /src

ARG HUGO_BASEURL="http://localhost:1313"
ENV HUGO_BASEURL ${BUILD_COMMAND}

# The entrypoint script supports commands "build", "server", or pass-through to sh.
ENTRYPOINT ["/src/entrypoint.sh"]

# Default operation
CMD ["build"]
