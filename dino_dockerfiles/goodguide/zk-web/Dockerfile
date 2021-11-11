FROM goodguide/base-oracle-java:8

# Set up Leiningen
ENV LEIN_ROOT ok
ENV LEIN_HOME /root/.lein
RUN mkdir $LEIN_HOME
ADD https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein /usr/bin/lein
RUN chmod +x /usr/bin/lein
# Init lein and ensure it's working before continuing
RUN lein version

RUN mkdir /build
WORKDIR /build

# Add project.clj and install deps
ADD project.clj /build/
RUN lein deps

# Then add the rest of the tree. (2-step approach helps avoid superfluous deps building)
ADD src/ /build/src
ADD resources/ /build/resources
ADD docker/wrapper.sh /usr/bin/wrapper.sh

# make sure things compile
RUN lein install

EXPOSE 8080

ENTRYPOINT ["/usr/bin/wrapper.sh"]
CMD ["lein", "run"]
