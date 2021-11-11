FROM ruby:2.3-alpine

ENV INTERSTELLAR_BASE=/usr/src/interstellar

RUN apk add --no-cache py-pip gcc make g++ git \
  && pip install boto \
  && gem install rest-client \
  && git clone https://github.com/ccyanni/interstellar.git /usr/src/interstellar

VOLUME ["/usr/src/interstellar/secrets"]

ENTRYPOINT ["ruby","-C","/usr/src/interstellar","/usr/src/interstellar/sender.rb"]
