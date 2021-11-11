FROM gfredericks/leiningen

RUN mkdir /usr/src/rdfsplit
WORKDIR /usr/src/rdfsplit

ADD project.clj ./
RUN lein deps

ADD . ./

RUN lein uberjar && cp target/uberjar/*-standalone.jar /usr/local/lib/ && rm -rf target

# Make launcher script
RUN echo "#!/bin/sh" > /usr/local/bin/rdfsplit
RUN echo "exec java -jar" /usr/local/lib/*-standalone.jar  '"$@"' > /usr/local/bin/rdfsplit
RUN chmod 755 /usr/local/bin/rdfsplit

RUN mkdir /data
WORKDIR /data
VOLUME /data

RUN /usr/local/bin/rdfsplit --help
CMD ["/usr/local/bin/rdfsplit" "--help"]
