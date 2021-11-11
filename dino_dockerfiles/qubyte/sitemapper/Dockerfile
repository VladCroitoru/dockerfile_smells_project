FROM golang

ADD . .
RUN go get github.com/PuerkitoBio/purell
RUN go get github.com/qubyte/sitemap
RUN go build

ENTRYPOINT ["./go"]