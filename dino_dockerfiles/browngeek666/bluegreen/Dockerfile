FROM node
RUN mkdir -p /app
WORKDIR /app

# Install app dependencies
RUN apt-get update
RUN apt-get install -y wget default-jre
RUN update-ca-certificates -f
RUN wget -O - -o /dev/null http://get.takipi.com/takipi-t4c-installer | bash /dev/stdin -i --sk=S19388#fVXmfNfc0wec5RE5#uR69LvTR0ufwb67kGqD44/Zv+nTSH2QJA6eFGGNcHIU=#dd1b
RUN /opt/takipi/etc/takipi-setup-machine-name browngeek666/bluegreen
RUN wget https://s3.amazonaws.com/app-takipi-com/chen/scala-boom.jar -O scala-boom.jar
CMD java -agentlib:TakipiAgent -jar scala-boom.jar

COPY package.json /app/
RUN npm install

COPY . /app

EXPOSE 80

ENTRYPOINT ["npm", "start"]
