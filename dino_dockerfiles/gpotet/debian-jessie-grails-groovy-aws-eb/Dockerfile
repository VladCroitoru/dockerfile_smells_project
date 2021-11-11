FROM re6exp/debian-jessie-oracle-jdk-8

RUN apt-get update
RUN apt-get -y install python-pip ca-certificates build-essential wget unzip python openssl zip curl
RUN pip install cryptography
RUN echo "import ssl" >> ssl.py
RUN python ssl.py
RUN pip install --upgrade awsebcli awscli
RUN curl -s get.sdkman.io | bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN source "$HOME/.sdkman/bin/sdkman-init.sh"
RUN yes | /bin/bash -l -c 'sdk install grails'
