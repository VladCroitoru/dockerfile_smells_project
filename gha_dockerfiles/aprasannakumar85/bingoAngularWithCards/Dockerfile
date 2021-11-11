FROM node:latest

RUN mkdir -p /app/src

WORKDIR /app/src

COPY package.json .

RUN npm install -g npm@7.24.1

COPY . .

#EXPOSE 4200

CMD ["npm", "start"]

#docker build . -t bingoangularwithcards:latest

#stop IIS before running the ap in port 80
#docker run -p 80:80 bingoangularwithcards

#docker run -p 4200:4200 bingoangularwithcards:latest

#https://dev.to/vanwildemeerschbrent/docker-angular-setup-issue-exposed-port-not-accessible-98m

#https://www.solutionsbyraymond.com/2019/12/26/deploy-angular-app-to-azure-container-instances/
