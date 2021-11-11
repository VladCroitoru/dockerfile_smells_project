FROM fedora:29 as builder

RUN dnf -y install \
	nodejs \
	golang \
	git \
	findutils \
	make && dnf clean all

RUN npm install -g less

ENV GOPATH /go
ENV PATH /go/bin:$PATH
RUN go get github.com/GeertJohan/go.rice/rice

WORKDIR /src
COPY . .

RUN make

FROM fedora:29
#RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

COPY --from=builder /src/wikinote /wikinote
EXPOSE 80
ENTRYPOINT ["/wikinote"]
CMD ["serve", "--bind", ":80"]
