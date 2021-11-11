# Imagem base
FROM node:14-alpine

# Configuração do usuário/permissões
USER node
RUN mkdir /home/node/todo-api
WORKDIR /home/node/todo-api

# Instalação das dependências
COPY package.json .
COPY yarn.lock .
RUN yarn install

# Copia dos arquivos do projeto
COPY . .

EXPOSE 3001

# Execução
CMD ["yarn", "test"]
