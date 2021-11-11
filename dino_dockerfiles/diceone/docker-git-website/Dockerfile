FROM nginx:alpine

RUN apk add openjdk8
RUN apk add git
RUN apk add rsync
RUN apk add bash
RUN mkdir -p /usr/local/bin/
COPY run-website /usr/local/bin/run-website
RUN chmod +x /usr/local/bin/run-website

CMD ["/usr/local/bin/run-website"]
