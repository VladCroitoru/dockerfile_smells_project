FROM clojure:alpine
MAINTAINER Christian Meter <meter@cs.uni-duesseldorf.de>

RUN apk --no-cache add yarn git python && \
    yarn global add bower node-sass && \
    mkdir ./discuss

WORKDIR /discuss
COPY . /discuss

RUN GIT_DIR=/tmp bower install --allow-root && \
    lein do clean, cljsbuild once min

WORKDIR /discuss/resources/public/

RUN node-sass css/discuss.sass css/discuss.css --style compressed && \
    node-sass css/zeit.sass css/zeit.css --style compressed && \
    rm -rf .sass-cache

EXPOSE 8080
CMD ["python2", "-m", "SimpleHTTPServer", "8080"]
