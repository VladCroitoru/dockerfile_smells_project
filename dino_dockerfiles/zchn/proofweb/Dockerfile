FROM ocaml/ocaml:ubuntu
MAINTAINER zchn

USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    gcc \
    wget \
    camlp4-extra \
    m4 libxstr-ocaml-dev libpcre-ocaml-dev libocamlnet-ocaml-dev \
    libxml-light-ocaml-dev camlp4-extra camlp5 make libapache2-mod-php5
RUN wget https://github.com/zchn/proofweb/archive/master.zip
RUN unzip master.zip
ENV CHROOT /
RUN make -C proofweb-master
