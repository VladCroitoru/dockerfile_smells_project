FROM node

# diretorio em que as informações ficam contidas
WORKDIR /usr/app

# copie o package para dentro desse diretorio: de onde ta vindo -> pra onde vai
COPY package.json ./

RUN yarn install

# copiar tudo pra dentro do diretorio raiz
COPY . .

EXPOSE 3333

#permitir rodar os comandos
CMD ["yarn", "run", "dev"]