FROM loadimpact/k6:latest AS k6official
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install sudo curl openssh-client -y
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install nodejs -y
COPY --from=k6official /usr/bin/k6 /usr/bin/k6
RUN npm install -g webpack-cli
RUN npm install -g webpack
RUN apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install docker-ce docker-ce-cli containerd.io -y
# install Docker Machine
RUN curl -L https://github.com/docker/machine/releases/download/v0.16.2/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine
RUN chmod +x /tmp/docker-machine
RUN cp /tmp/docker-machine /usr/local/bin/docker-machine
# I don't think that docker can be used without root access, so the following code has been removed
# RUN addgroup app && adduser -S -G app app
# RUN mkdir /app && chown app:app /app
# USER app
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run compile
EXPOSE 3002
CMD [ "npm", "start" ]