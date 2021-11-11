FROM michilu/docker-web-essentials

# gcc and musl-dev needed by the Go Race Detector
# GNU grep needed by the deploy step on Wercker CI
# openssh-client needed by the dep pulling private repository
RUN apk --no-cache --update add \
  gcc \
  musl-dev \
  grep \
  openssh-client \
  && mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
  ;

ENV \
  CGO_ENABLED="0" \
  GOPATH="/usr/local/go_appengine/gopath" \
  GOROOT="/usr/local/go_appengine/goroot-1.8" \
  PATH="/usr/local/go_appengine:/usr/local/go_appengine/goroot/bin:/usr/local/go/bin:$PATH"

RUN gae_version="1.9.70" \
  ;:`#; go_version="1.10.0"` \
  ; apk --no-cache --update add --virtual=build-time-only \
  curl \
  tar \
  && curl -s -o file.zip https://storage.googleapis.com/appengine-sdks/featured/go_appengine_sdk_linux_amd64-${gae_version}.zip \
  && unzip -qq file.zip -d /usr/local \
  && rm file.zip \
  && : ${go_version:=`goapp version|sed -e "s/^.*go version \([0-9\.]\+\).*$/\1/g"`} \
  ; curl -s https://storage.googleapis.com/golang/go${go_version}.linux-amd64.tar.gz \
  | tar xzfp - -C /usr/local/ \
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
