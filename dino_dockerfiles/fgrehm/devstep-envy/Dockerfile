FROM progrium/envy

ADD ./data /tmp/data
ADD ./scripts /bin/

COPY ./cmd/envyd.go /go/src/github.com/progrium/envy/cmd/envyd.go
COPY ./pkg/hterm/hterm.go /go/src/github.com/progrium/envy/pkg/hterm/hterm.go
RUN go get && go build -a -o /bin/envyd
