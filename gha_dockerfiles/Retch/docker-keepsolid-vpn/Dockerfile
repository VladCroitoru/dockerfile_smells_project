
FROM alpine:3.13

RUN apk --no-cache add privoxy wireguard-tools curl py3-pip chromium chromium-chromedriver
ADD entrypoint.sh /usr/local/bin/
ADD config /etc/privoxy/
RUN chmod +r /etc/privoxy/config && chmod +x /usr/local/bin/entrypoint.sh
RUN mv /etc/privoxy/default.filter.new /etc/privoxy/default.filter \
    && mv /etc/privoxy/user.filter.new /etc/privoxy/user.filter \
    && mv /etc/privoxy/match-all.action.new /etc/privoxy/match-all.action \
    && mv /etc/privoxy/default.action.new /etc/privoxy/default.action \
    && mv /etc/privoxy/user.action.new /etc/privoxy/user.action \
    && mv /etc/privoxy/regression-tests.action.new /etc/privoxy/regression-tests.action \
    && mv /etc/privoxy/trust.new /etc/privoxy/trust
RUN pip install unofficialkeepsolidvpn

ENV EMAIL=x
ENV PASSWORD=x
ENV COUNTRY=de
ENV DEVICE=x

VOLUME [ "/etc/wireguard" ]

COPY fetchwg.py /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8118

HEALTHCHECK --interval=1m --timeout=10s --retries=1 \
    CMD curl -sS --fail -x http://localhost:8118 http://cloudflare.com || exit 1