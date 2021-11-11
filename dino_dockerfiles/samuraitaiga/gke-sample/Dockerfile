FROM centos:7
ENV container docker
RUN yum install -y epel-release
RUN yum install -y git python-pip
RUN git clone https://github.com/samuraitaiga/gke-sample.git /opt/gke-sample
RUN pip install -r /opt/gke-sample/requirements.txt
EXPOSE 8080
