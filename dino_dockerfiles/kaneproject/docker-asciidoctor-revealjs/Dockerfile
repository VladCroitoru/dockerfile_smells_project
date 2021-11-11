FROM asciidoctor/docker-asciidoctor
RUN mkdir /root/project
COPY Gemfile /root/project
WORKDIR /root/project
RUN apk update && \
    apk add git ruby-dev cmake alpine-sdk bison flex glib-dev cairo-dev pango-dev gdk-pixbuf-dev libxml2-dev && \
    git clone -b 3.3.0 --depth 1 https://github.com/hakimel/reveal.js.git && \
    apk del -r --no-cache
RUN gem install --no-document bundler
RUN bundle config --local github.https true
RUN bundle --path=.bundle/gems --binstubs=.bundle/.bin
COPY docker-endpoint.sh /
RUN chmod u+x /docker-endpoint.sh
WORKDIR /documents
CMD /docker-endpoint.sh
