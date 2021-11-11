# Uma imagem já existente
FROM node
# Definimos a pasta e copiamos os arquivos
WORKDIR /usr/app
COPY package.json ./
# Instalamos as dependencias
RUN npm install
# Depois de baixar as dependências agora copia tudo para dentro da pasta raiz
COPY . .
# Qual porta queremos expor
EXPOSE 3333
# Executamos a aplicacao
CMD ["npm","run","dev"]