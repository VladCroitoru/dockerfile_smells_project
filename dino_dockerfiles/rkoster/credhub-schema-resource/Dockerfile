FROM ubuntu AS resource

RUN apt-get update && \
    apt-get install -yy gnupg2 apt-utils wget curl

RUN wget -q -O - https://raw.githubusercontent.com/starkandwayne/homebrew-cf/master/public.key | apt-key add - \
    && echo "deb http://apt.starkandwayne.com stable main" | tee /etc/apt/sources.list.d/starkandwayne.list \
    && apt-get update && apt-get install -y \
       jq \
       spruce \
       credhub-cli

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \
    apt-get install -y nodejs

RUN npm install -g ajv-cli

COPY assets/check     /opt/resource/check
COPY assets/in        /opt/resource/in
COPY assets/out       /opt/resource/out
COPY assets/common.sh /opt/resource/common.sh

FROM resource AS test
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk netcat

#
# ADD test/credhub/src/ /credhub
# WORKDIR /credhub
# ENV VERSION 100.0.1
# ENV GOPATH /
# RUN ./setup_dev_mtls.sh
# RUN ./gradlew --no-daemon assemble
#
# ADD test/ /tests
# WORKDIR /tests
# RUN ./start_credhub.sh && ./all.sh

FROM resource
