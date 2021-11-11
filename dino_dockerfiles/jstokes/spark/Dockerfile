FROM mesosphere/spark:1.6.1-6

MAINTAINER jeffecu88@gmail.com

RUN apt-get update && apt-get -y install curl

RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda-latest-Linux-x86_64.sh

ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda
RUN conda install -y \
    matplotlib \
    seaborn \
    numpy \
    scikit-learn \
    bokeh \
    pandas

RUN mkdir -p /opt/spark/lib

RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar \
  -o /opt/spark/lib/aws-java-sdk-1.7.4.jar

RUN curl http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.1/hadoop-aws-2.7.1.jar \
  -o /opt/spark/lib/hadoop-aws-2.7.1.jar

RUN mkdir -p /etc/hadoop/backup

RUN mv /etc/hadoop/*-site.xml /etc/hadoop/backup
