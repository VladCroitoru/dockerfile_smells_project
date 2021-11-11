FROM golang:latest
USER root
MAINTAINER { ildarworld <ildarworld@gmail.com> }
RUN apt-get update
RUN apt-get install -y git

ADD . $GOPATH/src/
RUN cd $GOPATH/src/


RUN git init 
RUN git clone https://github.com/ildarworld/goPingerRepo.git 
#RUN go install https://github.com/ildarworld/goPingerRepo.git
RUN go get -u github.com/tatsushid/go-fastping 
#    cd $GOPATH/goPingerRepo/pinger/pingGo.go && \
    
RUN go build $GOPATH/goPingerRepo/pinger/pingGo.go
    
    
#RUN git checkout dev
#RUN go get -u github.com/tatsushid/go-fastping
#RUN cd $GOPATH/src/pinger/
#RUN go build /$GOPATH/goPingerRepo/pinger/pingGo.go

#ENTRYPOINT /go/src/pinger/
#CMD ["./pingGo"]
ENV PORT 8080
EXPOSE 8080

#
#*
#!/**/
#!*.*