FROM alpine
# This docker image is used by the runner application
# to be able to execute clojurescript code snippets from
# an article.
RUN apk add --no-cache bash gawk sed grep bc coreutils git nodejs
RUN npm install -g lumo-cljs