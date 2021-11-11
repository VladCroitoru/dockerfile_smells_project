FROM openresty/openresty:1.13.6.1-alpine

RUN apk add --no-cache curl bash && mkdir /build && cd /build && \
 curl -sSL https://github.com/bungle/lua-resty-session/archive/v2.22.tar.gz | tar -zx && \
 curl -sSL https://github.com/pintsized/lua-resty-http/archive/v0.12.tar.gz | tar -zx  && \
 curl -sSL https://github.com/zmartzone/lua-resty-openidc/archive/v1.5.4.tar.gz | tar -zx && \
 curl -sSL https://github.com/SkyLothar/lua-resty-jwt/releases/download/v0.1.11/lua-resty-jwt-0.1.11.tar.gz | tar -zx && \
 cp -r */lib/resty/* /usr/local/openresty/lualib/resty/ && \
 curl -sSL 'https://npc.nos-eastchina1.126.net/dl/jq_1.5_linux_amd64.tar.gz' | tar -zx -C /usr/bin && \
 curl -sSL 'https://npc.nos-eastchina1.126.net/dl/jwks2pem.tar.gz' | tar -zx -C /usr/bin && \
 rm -rf /build

ADD openidc_v1.5.4-patch.lua /usr/local/openresty/lualib/resty/openidc.lua
ADD nginx.conf /usr/local/openresty/nginx/conf/
ADD setup.sh run-proxy.sh /
RUN chmod 0755 /setup.sh /run-proxy.sh
CMD [ "/run-proxy.sh" ]
