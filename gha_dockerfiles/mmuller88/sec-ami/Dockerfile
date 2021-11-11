FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install curl unzip git jq gnupg -y

# install node and yarn
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash -
RUN apt-get -y install nodejs
RUN npm install -g yarn
RUN npm install -g typescript
RUN npm install -g ts-node

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && ./aws/install

WORKDIR /root
RUN git clone https://github.com/mmuller88/cdk-prowler.git
RUN cd cdk-prowler && yarn add projen && npx projen

# RUN mkdir -p /etc/init.d
COPY commands.sh /etc/init.d/commands
RUN chmod +x /etc/init.d/commands
RUN update-rc.d commands defaults

# cleanup
RUN rm -f /home/ubuntu/.ssh/authorized_keys
RUN rm -f /root/.ssh/authorized_keys
ENTRYPOINT ["/etc/init.d/commands", "start"]