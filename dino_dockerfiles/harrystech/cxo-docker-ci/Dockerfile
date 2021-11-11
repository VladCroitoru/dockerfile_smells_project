ARG JDK_BASE_IMAGE=gcr.io/google-appengine/openjdk:9

# Pull base image
FROM ${JDK_BASE_IMAGE}

# Override the appengine entrypoint
ENTRYPOINT ["/bin/bash"]

# Apparently moving these arguments above the "FROM" statement
# blows away the values. Stupid docker.
ARG SBT_VERSION=1.1.5
ARG SCALA_VERSION=2.12.6

# Export values for sub container use
ENV SBT_VERSION=${SBT_VERSION}
ENV SCALA_VERSION=${SCALA_VERSION}

# Install baseline utility packages
RUN apt-get update \
    && apt-get install -y --fix-broken \
    && apt-get install -y --no-install-recommends dirmngr python curl sudo gnupg apt-transport-https git ssh tar gzip lsb-release software-properties-common awscli bc \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create harrys user for running commands non-root
RUN ["adduser", "--disabled-password", "--gecos", "", "harrys"]
RUN ["usermod", "-aG", "sudo", "harrys"]
RUN echo 'harrys ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/harrys
USER harrys
# Default path is HOME
WORKDIR /home/harrys

# Install SBT
RUN echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list \
    && sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 \
    && sudo apt-get update \
    && sudo apt-get install sbt \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*

# Install sbt
ENV SBT_HOME=/home/harrys/.sbt
RUN mkdir -p "$SBT_HOME"

# Force SBT to bootstrap SBT_HOME and the compiler interface
RUN mkdir -p /tmp/force-compile/project  \
  && cd /tmp/force-compile      \
  && mkdir -p src/main/scala    \
  && echo "sbt.version=$SBT_VERSION" > project/build.properties \
  && echo "scalaVersion := \"$SCALA_VERSION\"" > build.sbt \
  && echo 'object EmptyMain { def main(args: Array[String]): Unit = {}  }' > src/main/scala/EmptyMain.scala \
  && sbt compile \
  && cd ~/ \
  && sudo rm -fR /tmp/*

# Install Docker
RUN sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" \
    && curl -fsSL -o "docker-key.gpg" "https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg" \
    && sudo apt-key add "docker-key.gpg" \
    && rm "docker-key.gpg" \
    && sudo apt-get update \
    && sudo apt-get install -y --no-install-recommends docker-ce \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*

# Install PIP & AWS CLI
RUN sudo curl -O https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py --user \
    && echo "PATH=~/.local/bin:$PATH" >> ~/.bash_profile \
    && /home/harrys/.local/bin/pip install awscli --upgrade --user

# Add harrys user to the docker group
RUN sudo usermod -aG docker harrys

# Install gcloud tools
RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -cs) main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl -fsSL -o "gcloud-key.gpg" "https://packages.cloud.google.com/apt/doc/apt-key.gpg" \
    && sudo apt-key add "gcloud-key.gpg" \
    && rm "gcloud-key.gpg" \
    && sudo apt-get update \
    && sudo apt-get install -y --no-install-recommends google-cloud-sdk \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*
