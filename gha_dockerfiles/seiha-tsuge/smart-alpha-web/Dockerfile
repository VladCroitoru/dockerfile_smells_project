FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:14

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn

COPY . /app

CMD ["/bin/bash"]
