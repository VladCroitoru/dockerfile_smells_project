FROM ubuntu:latest
#CREATING USER AND RUNNING SSH
RUN apt-get update
RUN adduser darahas
RUN adduser darahas sudo
RUN echo darahas:3823 | chpasswd
RUN echo root:3823 | chpasswd
RUN apt-get install -y sudo && apt-get install -y openssh-server    
#adding directories
RUN mkdir -p /home/darahas/node/app
WORKDIR /home/darahas/node/app
COPY package*.json /home/darahas/node/app/
RUN mkdir -p /var/run/sshd
#Installing additional sources
RUN apt-get -y install gcc g++ curl make
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash -
RUN apt-get -y install nodejs
RUN apt-get install -y pdftk poppler-utils ghostscript tesseract-ocr
#final steps
RUN npm install
COPY . /home/darahas/node/app/
EXPOSE 3000
CMD ["npm","start"]