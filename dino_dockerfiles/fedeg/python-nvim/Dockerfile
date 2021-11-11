FROM debian:stretch
MAINTAINER Federico Gonzalez (https://github.com/fedeg/)

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get --force-yes install -y neovim python-dev python-pip python3 python3-pip python3-dev curl vim exuberant-ctags git ack-grep \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip3 install neovim pep8 flake8 pyflakes pylint isort

ADD config/init.vim /root/.config/nvim/
RUN timeout 5m nvim || true

CMD ["nvim", "/src"]
