FROM ubuntu:16.04
ENV REPOSITORY https://github.com/chuckbutler/dasroot-blog.git
ENV AWS_ACCESS_KEY_ID XXX
ENV AWS_SECRET_KEY YYY
ENV BUCKET www.example.com
ENV GOPATH /go/
ENV THEME Porto
RUN apt-get update && apt-get upgrade -y && apt-get install -y git python-pygments s3cmd
ADD https://github.com/spf13/hugo/releases/download/v0.16/hugo_0.16-1_amd64.deb /tmp/
RUN dpkg -i /tmp/hugo_0.16-1_amd64.deb && rm /tmp/hugo_0.16-1_amd64.deb
ADD build.sh /build.sh
CMD ["/build.sh"]
