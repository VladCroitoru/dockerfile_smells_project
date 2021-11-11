FROM debian

RUN apt update && apt install -y curl
RUN curl -L https://github.com/drone/drone-cli/releases/download/v0.8.4/drone_linux_amd64.tar.gz | tar zx
RUN install -t /usr/local/bin drone
