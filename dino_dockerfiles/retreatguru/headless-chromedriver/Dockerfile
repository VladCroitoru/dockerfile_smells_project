FROM alpine:edge

# install chromium and chromedriver
RUN apk add --no-cache \
    dumb-init \
    chromium \
    chromium-chromedriver

# replace chromium binary with a script that has some default options
RUN mv /usr/lib/chromium/chrome /usr/lib/chromium/chrome-bin
COPY chrome /usr/lib/chromium/

# run chromedriver under dumb-init to handle signals correctly
EXPOSE 4444
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["chromedriver", "--port=4444", "--whitelisted-ips="]
