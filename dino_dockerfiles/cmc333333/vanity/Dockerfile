FROM node:14.15.3-buster

RUN apt update \
    && apt -y install libgl1-mesa-glx libxi6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ["package.json", "package-lock.json", "/usr/src/app/"]
COPY ["plugins", "plugins"]   # referenced in the package.json file

ARG NODE_ENV
ENV NODE_ENV=$NODE_ENV
RUN npm install

COPY ["data", "data"]
COPY ["src", "src"]
COPY ["static", "static"]
COPY ["gatsby-config.js", "gatsby-node.js", "/usr/src/app/"]
