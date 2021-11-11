FROM ruby

RUN gem install redis-stat

COPY run.sh run.sh

EXPOSE 63790
CMD ./run.sh
