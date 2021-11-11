FROM java
MAINTAINER Olivier Filangi "olivier.filangi@inra.fr"

ENV FLUIDOPS="http://www.fluidops.com/downloads/collateral/"
ENV FEDX="FedX 3.1.zip"

#ENV fedx4askomics=https://github.com/ofilangi/askomics.git

# Prerequisites
RUN apt-get update && apt-get install -y \
  git \
  wget \
  vim \
  unzip \
  build-essential \
  python3 \
  python3-pip

RUN pip3 install py4j
RUN git config --global http.sslVerify false
#RUN git clone $ASKOMICS /usr/local/askomics/

RUN wget "$FLUIDOPS/$FEDX"
RUN unzip "$FEDX" -d /fedx

RUN mkdir /fedx4askomics
WORKDIR /fedx4askomics/
ADD ServiceFedXGateway.java .

RUN javac -cp /fedx4askomics/:$(ls /usr/local/share/py4j/py4j*.jar):/fedx/lib/* ServiceFedXGateway.java
RUN echo "#!/bin/bash\necho 'Run FedX - ServiceFedXGateway '\njava -cp /fedx4askomics/:$(ls /usr/local/share/py4j/py4j*.jar):/fedx/lib/* ServiceFedXGateway\n" > exec_fedxgateway.sh
RUN chmod +x exec_fedxgateway.sh

CMD ["/fedx4askomics/exec_fedxgateway.sh"]
