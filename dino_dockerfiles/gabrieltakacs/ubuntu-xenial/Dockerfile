FROM ubuntu:16.04
MAINTAINER Gabriel Takács <gtakacs@gtakacs.sk>

# Install common utilities
RUN apt-get update && \
    apt-get -y upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y bash zsh git grep sed curl wget tar gzip postfix ssh vim

CMD ["/bin/bash"]
