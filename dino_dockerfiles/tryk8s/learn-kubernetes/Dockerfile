FROM jupyter/notebook
RUN apt-get update;apt-get install -y openssh-client;ssh-keygen -f /root/.ssh/id_rsa -N "";echo "Host gogs\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
RUN curl -o /usr/bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.10.3;chmod +x /usr/bin/docker
RUN curl -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.2.2/bin/linux/amd64/kubectl;chmod +x /usr/bin/kubectl
ADD environment /etc/environment
ADD notebooks /notebooks
