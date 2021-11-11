FROM node:16-buster-slim

ENV NODE_ENV=production

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --production

COPY . .

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list \
    && apt-get update \
    && apt-get install -y wget \
    && apt-get install -y --no-install-recommends firefox -o APT::Immediate-Configure=0

RUN chmod +x install-geckodriver.sh

RUN sh ./install-geckodriver.sh

# Development
# EXPOSE 3000

CMD ["npm", "run", "start"]
