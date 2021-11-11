FROM openzim/zimwriterfs:latest

# Install package dependencies
RUN apt-get update && \
    apt-get -y install git curl

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install --yes nodejs

# Local Development
#COPY ./ /app

RUN \
    git clone https://github.com/openzim/zip2zim.git /app && \
    cd /app && \
    npm i
RUN cd /app && /usr/bin/npm run build

WORKDIR /app

EXPOSE 8000
ENTRYPOINT ["node"]
CMD ["./node_modules/.bin/pm2-docker", "build/index.js"]