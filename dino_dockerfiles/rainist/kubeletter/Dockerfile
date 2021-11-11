FROM clojure:lein-2.7.1

ENV KUBECTL_VERSION=v1.8.1

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl \
  && mv kubectl /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kubectl

RUN mkdir -p /code
WORKDIR /code
COPY kubeletter/project.clj /code
RUN lein deps

COPY kubeletter /code
CMD lein run
