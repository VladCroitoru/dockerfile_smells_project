FROM ruby:2.3-alpine

RUN apk update && \
    apk add make gcc g++ nodejs

RUN gem install bundler smashing
RUN smashing new dashboard

VOLUME ["/dashboard"]

RUN cd /dashboard && \
    bundle

ENV PORT 3030
EXPOSE $PORT

WORKDIR /dashboard

ENTRYPOINT ["smashing"]
CMD ["start", "-p", "$PORT"]
