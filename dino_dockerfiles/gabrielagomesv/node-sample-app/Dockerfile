# De onde esta vindo a img
# FROM linguagem .. versao
FROM node:carbon

# Diretório de execucao da aplicação
WORKDIR /usr/src/app

# Copiando dependencias do NODE
COPY package.json ./ 

# Instalando dependencias do NODE 
RUN npm install

# Copia tudo do diretorio corrente para o WORKDIR
COPY . $WORKDIR 

# Define qual porta o container deve escutar no build
EXPOSE 8080 

# Execucao da aplicacao usando CMD
CMD [ "npm", "start" ]