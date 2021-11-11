FROM python:3.8

# New project
WORKDIR /project

COPY requirements.txt requirements.txt

#COPY  . . opção para copiar tudo

# Utils
RUN apt-get -y update
RUN apt-get -y install wget curl vim net-tools
RUN apt-get -y install vim nano tree

## Install Java
RUN wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz -P /usr/local/.
RUN tar -xzvf /usr/local/jdk-8u131-linux-x64.tar.gz -C /usr/local/
RUN ln -s /usr/local/jdk1.8.0_131/ /usr/local/java
ENV JAVA_HOME "/usr/local/java"
ENV PATH "$JAVA_HOME/bin:$PATH"

# Python and Dependencies:
RUN pip3 -q install pip --upgrade && \
    pip3 install -r requirements.txt

# Install Tini
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

# Open jupyter notebook
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]

#CMD ["tail", "-f", "/dev/null"]
