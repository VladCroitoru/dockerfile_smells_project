
FROM alpine:3.11.7 as intermediate

ARG SSH_PRIVATE_KEY
ARG GITUSER
ARG GITPASSWORD

ENV GOPATH /go

COPY . /go/src/github.com/hound-search/hound

RUN apk update \
	&& apk add go git subversion libc-dev mercurial bzr openssh tini \
	&& cd /go/src/github.com/hound-search/hound \
	&& go mod download \
	&& go install github.com/hound-search/hound/cmds/houndc \
	&& go install github.com/hound-search/hound/cmds/houndd \
	&& apk del go \
	&& rm -f /var/cache/apk/* \
	&& rm -rf /go/src /go/pkg

RUN /go/bin/houndc -username ${GITUSER} -password ${GITPASSWORD} -outputfile ./config.json

RUN mkdir ~/.ssh/
RUN echo "${SSH_PRIVATE_KEY}" > ~/.ssh/id_ed25519
RUN chmod 600 ~/.ssh/id_ed25519
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts


FROM alpine:3.11.7

ENV GOPATH /go

RUN mkdir ~/.ssh/
COPY --from=intermediate /root/.ssh/id_ed25519 /root/.ssh/id_ed25519
COPY --from=intermediate /root/.ssh/known_hosts /root/.ssh/known_hosts

COPY --from=intermediate /go/bin/houndd ./go/bin/houndd

RUN apk update \
	&& apk add git subversion libc-dev mercurial bzr openssh tini 

COPY --from=intermediate /config.json ./config.json

VOLUME [ "/data" ]

EXPOSE 6080

ENTRYPOINT ["/sbin/tini", "--", "/go/bin/houndd", "-conf", "/config.json"]
