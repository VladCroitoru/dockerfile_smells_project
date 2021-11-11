FROM vangorra/burstcoin-plotter-docker

COPY simple_plot.sh /usr/local/bin

RUN apk --no-cache add bash findmnt

ENTRYPOINT ["/usr/local/bin/simple_plot.sh"]
