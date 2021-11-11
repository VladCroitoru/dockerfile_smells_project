FROM gliderlabs/alpine:3.1
RUN apk-install jq curl bash && rm -rf /var/cache/apk/*
ADD md-to-html.sh /
ENTRYPOINT ["/md-to-html.sh"]
CMD ["README.md"]
