FROM circleci/clojure:lein-2.8.1-node-browsers

MAINTAINER LifeCheq

USER root

RUN npm install --silent --global \
    karma-cli \
    firebase-tools \
    firebase-bolt

RUN echo '(defproject dummy "" :dependencies [[cljsbuild "1.1.7"]])' > project.clj \
  && lein deps && rm project.clj

USER circleci

RUN echo '(defproject dummy "" :dependencies [[cljsbuild "1.1.7"]])' > project.clj \
  && lein deps && rm project.clj

RUN curl -sL https://sentry.io/get-cli/ | bash