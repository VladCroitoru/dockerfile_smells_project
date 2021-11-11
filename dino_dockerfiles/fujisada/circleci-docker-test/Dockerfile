FROM centos:7

RUN curl "https://storage.googleapis.com/golang/go1.8.1.linux-amd64.tar.gz" > "/opt/go1.8.1.linux-amd64.tar.gz"
RUN tar -C /usr/local -xzf /opt/go1.8.1.linux-amd64.tar.gz

# set PATH
RUN echo "export GOPATH=/go" > /etc/profile.d/gopath.sh
RUN echo "export PATH=$GOPATH/bin:/usr/local/go/bin/:$PATH" >> /etc/profile.d/gopath.sh
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

# add libs
RUN yum -y install epel-release
RUN rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
RUN yum -y install —enable-repo=nux-dextop,epel git gcc libjpeg-turbo-devel ffmpeg-devel

# install glide
RUN yum -y install which
RUN mkdir -p "$GOPATH/bin" "$GOPATH/src"
RUN curl https://glide.sh/get | sh

# install aws cli
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"
RUN python /tmp/get-pip.py
RUN pip install awscli
