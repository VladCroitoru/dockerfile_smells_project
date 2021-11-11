FROM gliderlabs/alpine

RUN apk-install curl

COPY hakashiro /root/hakashiro
RUN chmod u+x /root/hakashiro

ENTRYPOINT ["/root/hakashiro"]
CMD ["dummy-token"]

