FROM jruby:9-alpine

RUN apk add --no-cache make gcc g++ python bash git openssh

ENV MEDA_THREADS 0:4
ENV MEDA_PORT 8000
ENV MEDA_ENV development
ENV JRUBY_OPTS -J-Xmx1g

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN bundle install && gem install puma

EXPOSE ${MEDA_PORT}

CMD puma --environment ${MEDA_ENV} --port ${MEDA_PORT} --threads ${MEDA_THREADS}