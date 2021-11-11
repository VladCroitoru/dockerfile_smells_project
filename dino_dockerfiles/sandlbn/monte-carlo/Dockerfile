FROM alpine:3.1
RUN apk --update add wget

RUN wget --no-check-certificate  http://github.com/sandlbn/monte-carlo/raw/master/monte_carlo
RUN chmod +x monte_carlo
RUN mv monte_carlo /bin/monte_carlo

RUN apk del wget
RUN rm /var/cache/apk/*

ENTRYPOINT ["/bin/monte_carlo"]
