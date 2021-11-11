FROM golang:1.8

RUN wget -q -O- 'https://download.ceph.com/keys/release.asc' | apt-key add - && \
    echo deb http://download.ceph.com/debian-hammer/ jessie main | tee /etc/apt/sources.list.d/ceph.list 

RUN apt-get update && apt-get install -y libpcap-dev python-netaddr sshpass python-pip python-dev build-essential libssl-dev libffi-dev jq vim nginx net-tools ceph-common
RUN go get -v github.com/google/gopacket
RUN go get -v github.com/simonschuang/cdxctl

RUN pip install --upgrade cffi
RUN pip install ansible ansible-cmdb

RUN wget https://storage.googleapis.com/kubernetes-release/release/v1.5.7/bin/linux/amd64/kubectl -O /usr/local/sbin/kubectl && chmod +x /usr/local/sbin/kubectl

RUN mkdir -p /etc/ansible
ADD ansible.cfg /etc/ansible/ansible.cfg

WORKDIR /root

CMD ["/bin/sleep", "infinity"]
