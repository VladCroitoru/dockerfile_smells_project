FROM jenkins

USER root

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN groupadd docker && gpasswd -a jenkins docker

RUN apt-get update && apt-get -y upgrade && apt-get install -y --no-install-recommends sudo dnsutils nodejs build-essential && apt-get clean && rm -r /var/lib/apt/lists/*

RUN curl -O https://storage.googleapis.com/kubernetes-release/release/v1.3.4/bin/linux/amd64/kubectl && mv ./kubectl /usr/bin/ && chmod +x /usr/bin/kubectl

RUN curl -O https://get.docker.com/builds/Linux/x86_64/docker-1.10.3 && mv ./docker-1.10.3 /usr/bin/docker && chmod +x /usr/bin/docker

RUN adduser jenkins sudo

RUN cd /opt && curl -O http://ftp.cixug.es/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz && tar -xvzf apache-maven-3.3.9-bin.tar.gz -C /opt && rm -f apache-maven-3.3.9-bin.tar.gz

ENV PATH $PATH:/opt/apache-maven-3.3.9/bin

RUN npm install -g browserify && npm install -g uglifyjs && npm install -g typescript

RUN curl -O https://storage.googleapis.com/golang/go1.7.3.linux-amd64.tar.gz && tar -xvzf go1.7.3.linux-amd64.tar.gz -C /usr/local && rm -f go1.7.3.linux-amd64.tar.gz

ENV PATH $PATH:/opt/apache-maven-3.3.9/bin:/usr/local/go/bin
ENV GOROOT /usr/local/go

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins
