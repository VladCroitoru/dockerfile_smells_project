FROM mhart/alpine-node-auto:8

RUN apk --no-cache --update add \
  bash \
  curl \
  git \
  make \
  rsync \
  mercurial \
  python \
;

ENV \
  CGO_ENABLED="0" \
  GOPATH="/usr/local/go_appengine/gopath" \
  GOROOT="/usr/local/go_appengine/goroot-1.8" \
  PATH="/usr/local/go_appengine:/usr/local/go_appengine/goroot/bin:/usr/local/go/bin:/usr/local/go_appengine/gopath/bin:$PATH"

RUN gae_version="1.9.57" \
  ; go_version="1.8.3" \
  ; zipfile="go_appengine_sdk_linux_amd64-${gae_version}.zip" \
  ; apk --no-cache --update add \
# gcc and musl-dev needed by the Go Race Detector
  gcc \
  musl-dev \
# GNU grep needed by the deploy step on Wercker CI
  grep \
# openssh-client needed by the dep pulling private repository
  openssh-client \
  && apk --no-cache --update add --virtual=build-time-only \
  curl \
  tar \
  && curl -sO https://storage.googleapis.com/appengine-sdks/featured/${zipfile} \
  && unzip -qq ${zipfile} -d /usr/local \
  && rm ${zipfile} \
  && : ${go_version:=`goapp version|sed -e "s/^.*go\([0-9\.]\+\).*$/\1/g"`} \
  ; curl -s https://storage.googleapis.com/golang/go${go_version}.linux-amd64.tar.gz \
  | tar xzfp - -C /usr/local/ \
  && mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
  && apk del build-time-only

CMD type go \
  && go version \
  && type goapp \
  && goapp version \
  && type gofmt \
  && type godoc \
  && echo -n "GOPATH: " \
  && goapp env GOPATH \
  && echo -n "GOROOT: " \
  && goapp env GOROOT \
;
