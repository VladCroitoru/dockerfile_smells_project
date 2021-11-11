FROM golang:latest
MAINTAINER Piotr Łuczak<piotrluczak1995@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
	texlive-base \
	texlive-lang-all \
&& apt-get clean

COPY template.tex .
COPY screens2pdf.go .
RUN go build screens2pdf.go

ENTRYPOINT ["./screens2pdf"]
