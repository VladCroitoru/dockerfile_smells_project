FROM gliderlabs/alpine:3.9@sha256:23b993692b943f0799b3f36042d8a1331557103eb4ac2c0b8ab36cab9f399f8b

ENV \
MYIP_VERSION='v0.3.4' \
MYIP_HASH='0c995b4e242740e7e9b71ee56b41e52e92362fcd9eac09159aa5ae69ef6526ba'

RUN \
apk --update add --no-cache \
  ca-certificates python3 jq curl && \
update-ca-certificates && \
pip3 install --no-cache-dir awscli && \
mkdir /lib64 && \
ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \
curl -fsSL "https://github.com/kitsuyui/myip/releases/download/${MYIP_VERSION}/myip_linux_amd64" > /usr/sbin/myip && \
echo "${MYIP_HASH}  /usr/sbin/myip" | sha256sum -s -c - && \
chmod +x /usr/sbin/myip

ADD main.sh /usr/bin/entrypoint
ENTRYPOINT entrypoint
