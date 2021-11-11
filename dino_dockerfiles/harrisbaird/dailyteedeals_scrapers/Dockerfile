FROM harrisbaird/scrapyd:py2

ENV BUILD_PACKAGES=build-base \
    RUNTIME_PACKAGES="libssl1.0"

WORKDIR /app

ADD requirements.txt /app

RUN apk --update --no-cache add $RUNTIME_PACKAGES && \
  apk add --virtual build-dependencies $BUILD_PACKAGES && \
  pip uninstall -y scrapyd && \
  pip --no-cache-dir install -r requirements.txt && \
  apk del build-dependencies

ADD . /app

# Run scrapyd and deploy project.
RUN scrapyd & PID=$! && \
  sleep 5 && \
  scrapyd-deploy && \
  kill $PID

EXPOSE 6800 6900

ENTRYPOINT ["supervisord", "-c", "supervisord.conf"]
