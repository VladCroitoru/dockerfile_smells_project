FROM gocd/gocd-agent-ubuntu-16.04:v18.1.0

#INSTALL JAVA 8
# Install the python script required for "add-apt-repository"
RUN apt-get update && apt-get install -y software-properties-common

# Install java8 (see digitalocean tutorial)
RUN apt-get install -y default-jre
RUN apt-get install -y default-jdk

# Setup JAVA_HOME, this is useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

#INSTALL MAVEN 3
ENV MAVEN_VERSION 3.5.2

RUN mkdir -p /usr/share/maven \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

# Install Docker CE
RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates software-properties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce=17.12.0~ce-0~ubuntu

# Install AWS CLI (~/.aws/credentials and ~/.aws/config need 2 be mounted)
ENV LC_ALL C

RUN apt-get install -y python-pip python-dev build-essential \
  && pip install --upgrade pip \
  && pip install --upgrade virtualenv \
  && pip install awscli --upgrade

# Install Node and NPM
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs

# Add go user to the docker group
RUN usermod -aG docker go

COPY settings.xml /home/go/.m2/

# Install Chrome
RUN curl -fsSL -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get -y update \
  && apt-get -y install google-chrome-stable

# Install ChromeDriver
RUN curl -fsSL http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip -o chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip \
  && mv -f chromedriver /usr/local/bin/chromedriver \
  && chown root:root /usr/local/bin/chromedriver \
  && chmod 0755 /usr/local/bin/chromedriver

# Install Groovy
RUN apt-get install -y groovy2