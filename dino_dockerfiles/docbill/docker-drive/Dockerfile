FROM fedora
MAINTAINER Bill C Riemers https://github.com/docbill

RUN dnf update -y && dnf install -y git go godep findutils sudo && dnf clean -y all

ENV GOPATH=/opt/work-go

ADD docker-drive.sh /usr/sbin/docker-drive

RUN useradd -m -d "/opt/work-go" work-go && chmod 500 /usr/sbin/docker-drive

USER work-go

RUN go get github.com/tools/godep && \
  go install github.com/tools/godep && \
  go get github.com/odeke-em/drive/drive-gen && \
  go get golang.org/x/sys/unix && \
  go get google.golang.org/appengine && \
  cd $GOPATH/src/github.com/odeke-em/drive/drive-gen/ && \
  git config --global user.email "nobody@nowhere.com" && \
  git config --global user.name "Noone" && \
  git rm -rf Godeps && \
  git commit -a -m 'rebuild dependancies' && \
  godep save && \
  godep restore && \
  git add Godeps && \
  git commit --amend -a -m 'rebuild dependancies' && \
  go install github.com/odeke-em/drive/drive-gen && \
  "$GOPATH/bin/drive-gen" && \
  chmod -R ugo+rX "$GOPATH"

USER root
ENV HOME=/drive
VOLUME /drive
WORKDIR /drive

ENTRYPOINT ["/usr/sbin/docker-drive"]

