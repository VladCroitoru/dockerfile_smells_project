FROM registry.fedoraproject.org/f25/etcd

RUN dnf install -y openssl curl

ADD run.sh /root/run.sh
RUN /bin/chmod +x /root/run.sh

CMD ["/root/run.sh"]
