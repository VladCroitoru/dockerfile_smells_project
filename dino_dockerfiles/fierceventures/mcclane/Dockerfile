FROM clojure

RUN apt-get update
RUN apt-get update --fix-missing
RUN apt-get install wget
RUN apt-get install sudo
RUN apt-get install -y vim

# Install Maven
RUN sudo apt-get install maven -y

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
RUN sudo apt-get install nodejs
RUN node -v
RUN npm -v

# Install Phantomjs
RUN sudo apt-get install build-essential chrpath libssl-dev libxft-dev -y
RUN sudo apt-get install libfreetype6 libfreetype6-dev -y
RUN sudo apt-get install libfontconfig1 libfontconfig1-dev -y
RUN wget https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN sudo tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN sudo mv phantomjs-2.1.1-linux-x86_64 /usr/local/share
RUN sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
RUN phantomjs --version

# Install Terraform
RUN wget https://releases.hashicorp.com/terraform/0.11.8/terraform_0.11.8_linux_amd64.zip
RUN unzip terraform_0.11.8_linux_amd64.zip
RUN sudo mv terraform /usr/local/bin/
RUN terraform --version

# Install AWS CLI & EB CLI
RUN sudo apt-get -y install python python-pip
RUN sudo pip install awscli
RUN pip install awsebcli
RUN aws --version

# Install Ruby and Bundler
RUN apt-get install -y ruby ruby-dev
RUN gem install bundler

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Install ChromeDriver.
RUN wget -N http://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip -P ~/
RUN unzip ~/chromedriver_linux64.zip -d ~/
RUN rm ~/chromedriver_linux64.zip
RUN mv -f ~/chromedriver /usr/local/bin/chromedriver
RUN chown root:root /usr/local/bin/chromedriver
RUN chmod 0755 /usr/local/bin/chromedriver

# Install Docker (Yo Dawg)
RUN apt-get install -y apt-transport-https ca-certificates curl software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian jessie stable"
RUN apt-get update
RUN apt-get install -y docker-ce

# Install Firebase tools
RUN npm install -g firebase-tools

# Install Karma
RUN npm install -g karma-cli@1.0.1

# Install shadow-cljs
RUN npm install -g shadow-cljs@2.4.1

# Install Google Cloud tools
RUN export CLOUD_SDK_REPO="cloud-sdk-stretch" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud config set pass_credentials_to_gsutil false && \
    gcloud --version && \
    gsutil --version

# Install Netcat (nc)
RUN apt-get install -y netcat

# Install PostgreSQL client (psql)
RUN apt-get install -y postgresql-client

# Install Flyway
ENV FLYWAY_VERSION 5.2.0

RUN mkdir /fw \
  && cd /fw \
  && curl -L https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz -o flyway-commandline-${FLYWAY_VERSION}.tar.gz \
  && tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz --strip-components=1 \
  && rm flyway-commandline-${FLYWAY_VERSION}.tar.gz

ENV PATH ${PATH}:/fw/

# Install jq
RUN apt-get install -y jq

# It's a good idea to use dumb-init to help prevent zombie chrome processes.
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init
CMD ["dumb-init", "--"]
