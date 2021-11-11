FROM    debian

ENV     TERM=xterm

RUN     apt-get update -yqq && apt-get install -yqq \
            git \
            cmake \
            nano

RUN     git clone https://github.com/jjaniec/fillit.git

WORKDIR fillit

RUN     git clone https://github.com/jjaniec/libft.git

RUN     make

RUN     make map T_COUNT=7

CMD     ["bash"]
