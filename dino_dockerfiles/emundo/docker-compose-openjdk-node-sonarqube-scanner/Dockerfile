FROM openjdk:11

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y apt-transport-https

# add Node.js source
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key \
        | apt-key add - \
    && sh -c 'echo "deb https://deb.nodesource.com/node_12.x stretch main" > /etc/apt/sources.list.d/nodesource.list' \
    && sh -c 'echo "deb-src https://deb.nodesource.com/node_12.x stretch main" >> /etc/apt/sources.list.d/nodesource.list' \
    && apt-get update -o Dir::Etc::sourcelist="sources.list.d/nodesource.list" \
        -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"

# add Google Chrome source
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub \
        | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update -o Dir::Etc::sourcelist="sources.list.d/google.list" \
        -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"

RUN apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        google-chrome-stable \
        libxss1 \
        gnupg2 \
        nodejs \
        software-properties-common \
        tar \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH "$PATH:/opt/google/chrome-unstable/"

RUN npm install -g npm@latest \
    && npm cache clean --force

## Docker Compose
RUN curl -sL "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

## Docker
RUN curl -sL "https://download.docker.com/linux/static/stable/$(uname -m)/docker-19.03.9.tgz" \
    | tar xzvf - -C /usr/local/bin/ --strip-components=1

RUN wget \
        "https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.3.0.2102-linux.zip" \
        -O ./sonar-scanner.zip; \
    jar xf sonar-scanner.zip; \
    mv sonar-scanner-* sonar-scanner; \
    rm sonar-scanner.zip; \
    rm sonar-scanner/**/*.bat; \
    mv sonar-scanner/bin/* /usr/local/bin; \
    mv sonar-scanner/lib/* /usr/local/lib; \
    rm -rf sonar-scanner; \
    chmod +x /usr/local/bin/sonar-*

## emundo User
RUN addgroup --gid 1101 rancher \
    # Für RancherOS brauchen wir diese Gruppe: http://rancher.com/docs/os/v1.1/en/system-services/custom-system-services/#creating-your-own-console
    && addgroup --gid 999 aws \
    # Für die AWS brauchen wir diese Gruppe
    && groupadd -r emundo \
    && useradd -rms /bin/bash \
        -g emundo \
        -G audio,aws,rancher,sudo,video \
        emundo \
    # FIXME Das ist notwendig, damit das Image lokal funktioniert
    && usermod -aG root emundo \
    && mkdir -p /home/emundo/Downloads

USER emundo
WORKDIR /home/emundo
