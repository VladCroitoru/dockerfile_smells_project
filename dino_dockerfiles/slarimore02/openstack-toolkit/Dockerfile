FROM ubuntu:16.04
RUN apt-get update && apt-get install -y mariadb-client python-dev python2.7 python-pip openssh-server \
    python-neutronclient python-glanceclient python-ironicclient python-manilaclient \
    python-novaclient python-swiftclient python-barbicanclient python-cinderclient \ 
    python-ceilometerclient python-heatclient python-troveclient
RUN pip install 'os-client-config==1.28.0'
RUN pip install 'python-openstackclient==3.12.0'
RUN mkdir /var/run/sshd
RUN mkdir -p /root/.ssh

EXPOSE 22

COPY docker/entrypoint.sh /

CMD ["/entrypoint.sh"]
