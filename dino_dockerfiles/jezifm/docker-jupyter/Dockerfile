FROM jupyter/notebook

# install Ubuntu dependencies
RUN apt-get update && apt-get -y install \
    graphviz \
    software-properties-common

# install Java
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN pip install iplantuml
COPY plantuml.jar /usr/local/bin/plantuml.jar
EXPOSE 8888
CMD ["jupyter", "notebook"]
