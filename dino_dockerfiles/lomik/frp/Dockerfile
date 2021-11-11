FROM alpine

RUN apk --no-cache add wget ca-certificates bash && \
    wget https://github.com/fatedier/frp/releases/download/v0.27.1/frp_0.27.1_linux_amd64.tar.gz && \
    tar xf frp_0.27.1_linux_amd64.tar.gz && \
    mkdir -p /opt/frp && \
    install -m 0755 frp_0.27.1_linux_amd64/frps /opt/frp/frps && \
    install -m 0755 frp_0.27.1_linux_amd64/frpc /opt/frp/frpc && \
    rm -rf frp*

COPY entrypoint.sh /opt/frp/entrypoint.sh

ENTRYPOINT ["/opt/frp/entrypoint.sh"]
