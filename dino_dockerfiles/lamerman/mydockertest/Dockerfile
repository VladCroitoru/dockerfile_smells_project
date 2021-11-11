FROM ubuntu
RUN apt-get install wget -y
RUN wget "https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz"
RUN tar -C /usr/local -xzf go1.4.2.linux-amd64.tar.gz
ENV PATH /usr/local/go/bin:$PATH
COPY server.go .
