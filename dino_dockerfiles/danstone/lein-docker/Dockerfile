
FROM danstone/jdk7-docker

RUN apt-get update
RUN apt-get install -y wget maven

RUN wget --no-check-certificate -O /usr/local/bin/lein https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
RUN chmod a+x /usr/local/bin/lein
ENV LEIN_ROOT true
VOLUME ["/root/.m2"]

RUN lein upgrade
