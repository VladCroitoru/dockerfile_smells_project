FROM    debian:stable

LABEL   maintainer="jjaniec@student.42.fr"

ENV     TERM=xterm

RUN     apt-get update -yqq && apt-get install -yqq --no-install-recommends \
            git \
            build-essential \
            nano \
            ca-certificates \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /root

RUN     git clone https://github.com/jjaniec/ft_ls.git

WORKDIR /root/ft_ls

RUN     make

CMD     ["bash"]
