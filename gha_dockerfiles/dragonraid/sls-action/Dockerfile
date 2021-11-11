FROM node:14

LABEL owner="Lukas Novotny <lucass.novotny@gmail.com>" \
      description="Runs serverless commands"

# Install docker as AWS Lambda also supports to use custom runtime, that is build via docker.
RUN apt-get update \
    && apt-get install -y \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg \
      lsb-release \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo \
      "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
      $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get install -y docker-ce docker-ce-cli containerd.io

WORKDIR /app

COPY . .

RUN npm install

ENTRYPOINT [ "/app/entrypoint.sh" ]
