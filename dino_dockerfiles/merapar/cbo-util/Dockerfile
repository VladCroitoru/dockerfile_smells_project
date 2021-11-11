FROM ubuntu
LABEL author="Alexandre Walzberg <alexandre.walzberg@merapar.com>"
RUN apt-get update && apt-get install -y python-pip redis-tools curl wget iputils-ping dnsutils vim nano && apt-get upgrade -y
RUN pip install --upgrade pip==9.0.1 && pip install awscli --upgrade
RUN useradd -ms /bin/bash cbo
COPY ./cluster-delete.sh /home/cbo
COPY ./cluster-keys.sh /home/cbo
RUN chmod +x /home/cbo/cluster-delete.sh
RUN chmod +x /home/cbo/cluster-keys.sh
USER cbo
WORKDIR /home/cbo
CMD ["/bin/bash"]
