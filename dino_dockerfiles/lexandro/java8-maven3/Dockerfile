FROM lexandro/java8-base

MAINTAINER Robert Stern <lexandro2000@<you know that big search company>.com

COPY apache-maven-3.3.3-bin.tar.gz /

RUN  tar xvf /apache-maven-3.3.3-bin.tar.gz -C /

ENV M2_HOME /apache-maven-3.3.3

ENV PATH $M2_HOME/bin:$PATH

WORKDIR /app

ENTRYPOINT ["mvn"]

