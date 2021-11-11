FROM alpine:latest
WORKDIR /frp/frp_0.37.1_linux_amd64
ADD https://github.com/fatedier/frp/releases/download/v0.37.1/frp_0.37.1_linux_amd64.tar.gz /frp/
ADD ./start.sh /frp/
RUN tar zxf /frp/frp_0.37.1_linux_amd64.tar.gz -C /frp/ \
    && chmod +x /frp/frp_0.37.1_linux_amd64/frps \
    && chmod +x /frp/frp_0.37.1_linux_amd64/frpc \
    && chmod +x /frp/start.sh
ENTRYPOINT ["sh", "/frp/start.sh"]