FROM fedora:latest

RUN dnf install -y \
  python \
  ansible \
  docker \
  python-docker-py \
  python-httplib2 \
  python-requests \
  python-dns \
  python-websocket-client

RUN pip install python-etcd==0.4.3

#Install kubectl
ADD https://storage.googleapis.com/kubernetes-release/release/v1.1.8/bin/linux/amd64/kubectl /usr/local/bin/
RUN chmod 755 /usr/local/bin/kubectl
