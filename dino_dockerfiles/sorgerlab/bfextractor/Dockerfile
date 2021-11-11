FROM continuumio/miniconda3:4.5.12

RUN apt-get update && apt-get install -y gcc openjdk-8-jdk && rm -rf /var/lib/apt/lists/*
RUN conda install cython boto3 scikit-image
RUN pip install -q pyjnius==1.2.1
RUN curl -o /opt/loci_tools.jar https://downloads.openmicroscopy.org/bio-formats/5.8.2/artifacts/loci_tools.jar

COPY bfextractor.py /opt

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV CLASSPATH /opt/loci_tools.jar
WORKDIR /tmp/aws

ENTRYPOINT ["python", "/opt/bfextractor.py"]
