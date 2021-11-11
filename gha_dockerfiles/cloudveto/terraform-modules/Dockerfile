FROM ubuntu:latest
COPY . ./
RUN apt-get -y update; apt-get -y install git curl jq python3-pip wget unzip && \
    pip3 install -U awscli ansible msrest msrestazure && \
    curl -fsSL https://get.docker.com -o get-docker.sh && \
    curl -L https://raw.githubusercontent.com/warrensbox/terraform-switcher/release/install.sh | bash && \
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.5.0.2216-linux.zip && \
    unzip sonar-scanner-cli-4.5.0.2216-linux.zip
