FROM fluent/fluent-bit:1.8

COPY fluent-bit.conf /fluent-bit/etc/fluent.conf
COPY myparsers.conf /fluent-bit/etc/myparsers.conf

EXPOSE 10224
EXPOSE 10514/udp

ENV TO_HOST logserver.example.com
ENV APP_NAME noname

CMD ["/fluent-bit/bin/fluent-bit", "-c", "/fluent-bit/etc/fluent.conf"]
