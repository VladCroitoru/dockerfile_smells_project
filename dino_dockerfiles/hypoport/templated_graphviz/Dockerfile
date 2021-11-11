FROM alpine:3.7
MAINTAINER Hypoport 

RUN apk update; apk add bash graphviz jq python2 py2-pip 
RUN apk add ttf-dejavu ttf-opensans ttf-freefont ttf-inconsolata ttf-liberation
RUN pip install j2cli

RUN mkdir -p /templated_graphviz
WORKDIR /templated_graphviz
VOLUME /templated_graphviz/rendering

COPY dot_templates ./dot_templates
COPY json_data ./json_data
COPY compile .

ENTRYPOINT ["/templated_graphviz/compile"]

