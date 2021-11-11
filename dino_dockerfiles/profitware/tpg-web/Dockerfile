# start from base
FROM clojure:alpine
MAINTAINER Sergey Sobko <S.Sobko@profitware.ru>

RUN mkdir -p /opt/tpg-web/target/default/stale

RUN addgroup -g 1000 -S appuser && \
    adduser -u 1000 -S appuser -G appuser

RUN chown -R appuser:appuser /opt/tpg-web
RUN chmod -R u+w /opt/tpg-web/target

USER appuser

# copy our application code
ADD . /opt/tpg-web
WORKDIR /opt/tpg-web

RUN lein deps

# expose port
EXPOSE 5000

# start app
CMD [ "lein", "run" ]
