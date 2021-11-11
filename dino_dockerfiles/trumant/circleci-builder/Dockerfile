FROM elixir:1.3.4
MAINTAINER Travis Truman <trumant@gmail.com>

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV PATH /opt/google-cloud-sdk/bin:$PATH

USER root

# Install google-cloud-sdk
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/chrome.list && \
  curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
  echo deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main > /etc/apt/sources.list.d/pgdg.list && \
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
  apt-get update -y && \
  apt-get install -y jq git make curl google-cloud-sdk kubectl postgresql-client-9.5 && \
  apt-get install -y unzip libnss3 libasound2 libgtk-3-0 libxss1 libxtst6 fonts-liberation libappindicator1 xdg-utils google-chrome-stable && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/*

# Install Chromedriver
RUN curl -o /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip && \
  unzip -d /usr/local/bin /tmp/chromedriver_linux64.zip && \
  rm /tmp/chromedriver_linux64.zip

# Install Docker
RUN curl -L -o /tmp/docker-17.05.0-ce.tgz https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz && \
  tar -xz -C /tmp -f /tmp/docker-17.05.0-ce.tgz && \
  mv /tmp/docker/* /usr/bin

# Install Helm
RUN wget http://storage.googleapis.com/kubernetes-helm/helm-v2.5.0-linux-amd64.tar.gz -P /tmp
RUN tar -zxvf /tmp/helm-v2.5.0-linux-amd64.tar.gz -C /tmp && mv /tmp/linux-amd64/helm /bin/helm && rm -rf /tmp
