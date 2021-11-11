FROM ubuntu AS builder

RUN apt update -y
RUN apt upgrade -y

RUN apt install -y locales
RUN apt install -y sudo

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "LANG=en_US.UTF-8" > /etc/locale.conf && \
    locale-gen en_US.UTF-8

RUN useradd -m -G sudo developer
RUN echo 'developer:developer' | chpasswd

USER developer

RUN echo developer | sudo -S DEBIAN_FRONTEND="noninteractive" apt install -y golang
RUN echo developer | sudo -S apt install -y ca-certificates && sudo update-ca-certificates
RUN echo developer | sudo -S apt install -y make git

ENV GOPATH /home/developer/go
ENV PATH $PATH:/home/developer/go/bin

COPY . /home/developer/go/src/github.com/mispon/tiktok-reporting-api
RUN echo developer | sudo -S chown -R developer /home/developer/

WORKDIR /home/developer/go/src/github.com/mispon/tiktok-reporting-api
RUN make build

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /home/developer/go/src/github.com/mispon/tiktok-reporting-api/bin/ .
RUN chown root:root tiktok-reporting-api
EXPOSE 80
ENTRYPOINT ["./tiktok-reporting-api"]