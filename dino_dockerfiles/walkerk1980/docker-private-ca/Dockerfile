FROM ubuntu
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::="--force-confnew" --assume-yes -y --yes -f dist-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::="--force-confnew" --assume-yes -y --yes -f install -y openssl dnsutils nano tcpdump screen tmux python-pip groff
RUN /usr/bin/pip install awscli
WORKDIR /root/
COPY ca /root/ca
COPY pca /root/pca
COPY openssl_root.cnf /root/ca/openssl_root.cnf
WORKDIR /root/ca/
ENV PASSWORD=Password1
ENV DOMAIN=example.com
ENV PCASUBJECT=CAtest1.example.com
ENV REGION=us-west-2
COPY createPCA.sh /usr/local/bin/createPCA.sh
COPY signPCA.sh /usr/local/bin/signPCA.sh
COPY startup.sh /usr/local/bin/startup.sh
COPY createCA.sh /usr/local/bin/createCA.sh
COPY cainfo.sh /usr/local/bin/cainfo.sh
COPY doitallforme.sh /usr/local/bin/doitallforme.sh
RUN /usr/local/bin/createCA.sh
