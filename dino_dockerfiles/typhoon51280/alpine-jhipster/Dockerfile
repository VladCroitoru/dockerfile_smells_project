FROM typhoon51280/alpine-node-java8

# install utilities
RUN apk add --update bash vim git sudo zip bzip2 fontconfig curl openssh make gcc g++ python linux-headers paxctl libgcc libstdc++ && \
    rm /var/cache/apk/*

# Setup SSH
# RUN mkdir -p ~root/.ssh && chmod 700 ~root/.ssh/ && \ 
#     chown -R root:root ~/.ssh && chmod 700 ~/.ssh/ && chmod 600 ~/.ssh/* && \
RUN  ssh-keygen -A && \
    sed -i 's/^#Port 22.*/Port 22/' /etc/ssh/sshd_config && \
    sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#UseDNS.*/UseDNS no/' /etc/ssh/sshd_config && \
    rc-update add sshd

# install maven
RUN MAVEN_VERSION=3.3.3 \
 && cd /usr/share \
 && wget -q http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \
 && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
 && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

# install yeoman
RUN npm install -g yo bower grunt-cli

# install JHipster
RUN npm install -g generator-jhipster

# configure the "jhipster" and "root" users
RUN addgroup jhipster && \
    adduser -S -s /bin/bash -G jhipster jhipster
RUN echo '%jhipster ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/jhipster
RUN echo 'root:jhipster' | chpasswd
RUN echo 'jhipster:jhipster' | chpasswd

# install the sample app to download all Maven dependencies
RUN cd /home/jhipster && \
    wget https://github.com/jhipster/jhipster-sample-app/archive/v2.22.0.zip && \
    unzip v2.22.0.zip && \
    rm v2.22.0.zip
RUN cd /home/jhipster/jhipster-sample-app-2.22.0 && npm install
RUN cd /home && chown -R jhipster:jhipster /home/jhipster
RUN cd /home/jhipster/jhipster-sample-app-2.22.0 && sudo -u jhipster mvn dependency:go-offline
RUN ln -s /home/jhipster/jhipster-sample-app-2.22.0 /home/jhipster/jhipster-sample-app

 
 # expose the working directory, the Tomcat port, the BrowserSync ports, the SSHD port, and run SSHD
VOLUME ["/jhipster"]
EXPOSE 8080 3000 3001 22


#ENTRYPOINT ["java"]
CMD  ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]
