FROM centos
WORKDIR /opt
RUN yum install git wget -y
RUN wget https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz
RUN tar -xf go1.9.2.linux-amd64.tar.gz
RUN rm -rf go1.9.2.linux-amd64.tar.gz
RUN git clone https://github.com/rsridivya/helloworld.git
WORKDIR /opt/helloworld/
RUN /opt/go/bin/go build hello.go
ENV PATH="${PATH}:/opt/helloworld"
EXPOSE 8080

