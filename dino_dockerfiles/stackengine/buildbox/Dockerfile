FROM oraclelinux:6.6
# on centos, yum install -y epel-release
# but on oraclelinux
RUN yum install -y http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

RUN yum install -y docker-io wget 
RUN yum install -y bzr patch s3cmd mercurial git sqlite-devel tar bash make ssh gcc

# for fpm
RUN yum install -y rpm rpm-build ruby-devel rubygems
RUN wget http://rpms.southbridge.ru/rhel6/ruby-1.9.3/x86_64/ruby-1.9.3.p547-1.el6.x86_64.rpm
RUN yum install -y ruby-1.9.3.p547-1.el6.x86_64.rpm
RUN gem install fpm

# download go 1.4.x needed for bootstrapping cloudflare 1.5 to /root/go1.4/
RUN curl -s https://storage.googleapis.com/golang/go1.4.3.linux-amd64.tar.gz | tar -vxz --xform 's|^go|go1.4|' -C /root
RUN mkdir -p /usr/local/src && cd /usr/local/src && git clone --branch go1.5.3-cloudflare1 https://github.com/cloudflare/go.git
RUN cd /usr/local/src/go/src && ./all.bash

# patch bzr's python lib, it has issues https://bugzilla.redhat.com/show_bug.cgi?id=1253897
COPY bzr.patch /usr/lib64/python2.6/site-packages/bzr.patch
RUN patch -d /usr/lib64/python2.6/site-packages -p0 < /usr/lib64/python2.6/site-packages/bzr.patch

RUN adduser stackengine
RUN mkdir -p /go/src/orahub.oraclecorp.com/opc-cs-dev/occs/controller && mkdir -p /go/{bin,pkg}
ENV GOPATH /go
ENV GO15VENDOREXPERIMENT 1
ENV PATH /go/bin:/usr/local/src/go/bin:$PATH

# download golint
RUN go get -u github.com/golang/lint/golint && \
	cd /go/src/github.com/golang/lint/ && \
	git checkout 32a87160691b3c96046c0c678fe57c5bef761456 && \
	go install ./golint

# download and install npm, gulp, karma for the ui nodejs
RUN yum -y install gcc gcc-c++ make flex bison gperf ruby \
	openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \
	libpng-devel libjpeg-devel && \
	curl --silent --location https://rpm.nodesource.com/setup_5.x | bash - && \
	yum -y install nodejs && \
	npm install -g gulp && \
	npm install -g karma

WORKDIR /go/src/orahub.oraclecorp.com/opc-cs-dev/occs
RUN chown stackengine:stackengine -R /go
USER stackengine
