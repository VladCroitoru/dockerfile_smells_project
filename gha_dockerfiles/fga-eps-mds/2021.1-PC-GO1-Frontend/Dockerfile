# define a imagem base
FROM node:14.17.6

# cria o diretório de trabalho
WORKDIR /code

# as instruções ADD, COPY, CMD, ENTRYPOINT ou RUN serão executadas no diretório de trabalho definido anteriormente

# copia os arquivos utilizados na instalação de dependências para o diretório de trabalho
COPY ./sysarq/package.json ./sysarq/yarn.lock /code/

# instala as dependências do projeto
RUN yarn

# copia o restante do projeto para o diretório de trabalho
COPY ./sysarq /code/
