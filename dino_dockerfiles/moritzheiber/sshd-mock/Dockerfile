FROM alpine:3.5

ENV RELEASE="v0.0.4"

ADD https://github.com/moritzheiber/sshd-mock/releases/download/${RELEASE}/sshd-mock_linux_amd64 sshd-mock
RUN chmod +x sshd-mock

EXPOSE 2222

CMD ["/sshd-mock"]
