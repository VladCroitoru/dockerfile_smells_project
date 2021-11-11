# Imagem base do container
FROM node

# Diretório com as informações, onde vai ficar a imagem
WORKDIR /user/app
# Copia o package.json local para dentro da pasta /user/app
COPY package.json /user/app/

RUN npm install

# Copia tudo para dentro da pasta raiz
COPY . /user/app

# Porta
EXPOSE 3333

# Rodar os camandos que precisam rodar
CMD ["npm","start"]