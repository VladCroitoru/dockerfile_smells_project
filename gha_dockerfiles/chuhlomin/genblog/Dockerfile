FROM golang:1.16 as build-env

WORKDIR /go/src/app
ADD . /go/src/app

RUN go get -d -v ./...
RUN go build -o /go/bin/app


FROM gcr.io/distroless/static:966f4bd97f611354c4ad829f1ed298df9386c2ec
# latest-amd64 -> 966f4bd97f611354c4ad829f1ed298df9386c2ec
# https://github.com/GoogleContainerTools/distroless/tree/master/base

LABEL name="render-template"
LABEL repository="http://github.com/chuhlomin/render-template"
LABEL homepage="http://github.com/chuhlomin/render-template"

LABEL maintainer="Konstantin Chukhlomin <mail@chuhlomin.com>"
LABEL com.github.actions.name="GenBlog"
LABEL com.github.actions.description="Generate a static blog from markdown files"
LABEL com.github.actions.icon="book"
LABEL com.github.actions.color="purple"

COPY --from=build-env /go/bin/app /app

CMD ["/app"]
