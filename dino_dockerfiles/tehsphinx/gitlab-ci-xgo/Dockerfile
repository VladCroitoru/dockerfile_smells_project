FROM golang:1.10

USER root

RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.03.1-ce.tgz && \
tar --strip-components=1 -xvzf docker-17.03.1-ce.tgz -C /usr/local/bin

RUN touch /root/.bashrc && \
echo "chown -R daemon:daemon /var/run/docker.sock" >> /root/.bashrc

RUN go get github.com/karalabe/xgo

CMD ["bash"]
