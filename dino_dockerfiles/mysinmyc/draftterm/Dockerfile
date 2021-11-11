FROM golang:1.7.1-wheezy

#Create target dirs
RUN mkdir -p /opt/draftTerm/etc /opt/draftTerm/bin /opt/draftTerm/src


#Compile
ENV PATH /usr/local/go/bin:$PATH
ENV GOPATH /opt/draftTerm

ADD . /opt/draftTerm/src/github.com/mysinmyc/draftTerm

RUN go get -t github.com/mysinmyc/draftTerm/cmd/draftTermd

#Compile generate_cert utility 
RUN cd $GOPATH/bin \
	&& go build /usr/local/go/src/crypto/tls/generate_cert.go


#Configure for container runtime
ADD ./sh/runContainer.sh /opt/draftTerm/bin

RUN useradd -m guest -s /bin/bash \
	&& echo guest:changeIt1! | chpasswd 

EXPOSE 8443

ENTRYPOINT ["/opt/draftTerm/bin/runContainer.sh"]

