FROM node:argon

#Clone repo to root directory
RUN cd / && git clone https://github.com/singh1469/dead-mans-snitch-cli.git

#Directory from which to run commands
WORKDIR /dead-mans-snitch-cli/app

#Install deps
RUN npm install

#Make script executable
RUN chmod 700 ./run.sh
