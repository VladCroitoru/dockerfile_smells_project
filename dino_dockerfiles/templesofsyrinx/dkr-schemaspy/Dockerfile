FROM java:8-jre
MAINTAINER John J. Chambers-Malewig

ENV SCHEMASPY_VERSION 5.0.0
ENV GRAPHVIZ_VERSION 2.38.0-7

# Update and install GraphViz as root
RUN apt-get update && \
    apt-get install -y \
        graphviz=${GRAPHVIZ_VERSION} \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/*

# Create schemaSpy to execute command with limited permissions
RUN useradd schemaSpy --create-home

USER schemaSpy

WORKDIR /home/schemaSpy/workdir

COPY schemaSpy_${SCHEMASPY_VERSION}.jar /home/schemaSpy/lib/schemaSpy.jar

USER root

ENTRYPOINT [ "java", "-jar", "/home/schemaSpy/lib/schemaSpy.jar" ]

CMD [ "--help" ]
