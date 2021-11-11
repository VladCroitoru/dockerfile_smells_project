FROM golang:1.11


RUN echo 'Synchronizing References in apt-get...'
RUN apt-get update

RUN echo 'Installing Unzip...'
RUN apt-get install unzip -y

RUN echo 'Installing mysql client'
RUN apt-get -y install mysql-client

RUN echo 'Grabbing AWS CLI...'
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip
RUN unzip awscli-bundle.zip

RUN apt -y install jq

RUN echo 'Installing AWS CLI...'
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
RUN rm -rf awscli-bundle*

# install tools
RUN go get github.com/golang/mock/gomock
RUN cd $GOPATH/src/github.com/golang/mock/gomock && git checkout bcfe3c1f21d5271939479786888af1338fa1b25c && go get github.com/golang/mock/gomock/...
RUN go install github.com/golang/mock/mockgen
RUN go get github.com/ilkka/substenv
RUN go get -u github.com/mizoguche/migorate
RUN go get -u github.com/golang/dep/...
RUN go get -u github.com/goadesign/goa
RUN go get -u github.com/goadesign/goa/goagen
RUN cd $GOPATH/src/github.com/goadesign/goa && git checkout v1.4.0 && go get github.com/goadesign/goa/goagen/... && go install github.com/goadesign/goa/goagen
RUN go get -u golang.org/x/lint/golint
RUN go get -u golang.org/x/tools/cmd/goimports

CMD /bin/sh
