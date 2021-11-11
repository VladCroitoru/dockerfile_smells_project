FROM golang:1.7.3

# 
ENV MY_PROJECT /myproject
RUN mkdir $MY_PROJECT

# gopath設定
RUN mkdir -p $MY_PROJECT/gopath
ENV GOPATH $MY_PROJECT/gopath
ADD ./gopath $GOPATH

# goプログラム設定
RUN mkdir -p $MY_PROJECT/golang
RUN cp -r  /usr/local/go/ $MY_PROJECT/golang/


RUN mkdir -p $GOPATH/bin
# path設定
ENV PATH $GOPATH/bin:$MY_PROJECT/golang/go/bin:$PATH


# Unix syslog delivery error
# https://groups.google.com/a/codenvy.com/d/msg/codenvy/6K6SgvK09oQ/oPswTD5aCAAJ
RUN apt-get update -q &&  apt-get install -y rsyslog
CMD /usr/sbin/rsyslogd -n 


# サービスとしては必要ないが、調査したいときがあるため入れておきたい
#RUN apt-get update && apt-get install -y net-tools
#WORKDIR $GOPATH/src/gozen





