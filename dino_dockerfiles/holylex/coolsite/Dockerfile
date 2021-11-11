FROM ubuntu:14.04
MAINTAINER Alexandre Perez "holylex@gmail.com"

RUN apt-get update


RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:ansible/ansible
RUN apt-get update
RUN apt-get install -y ansible
RUN apt-get install -y git
RUN apt-get install -y curl
#this add forces the use of no cache for the curl command
ADD Dockerfile Dockerfile 
RUN curl -sSL https://github.com/holylex/coolsite_config/archive/master.tar.gz | tar -xzv
RUN mv -f coolsite_config-master/hosts /etc/ansible/hosts
RUN ansible-playbook coolsite_config-master/local.yml -c local
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
EXPOSE 80

CMD ["nginx"]


