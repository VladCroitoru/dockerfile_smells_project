FROM heroku/heroku:20

# Define pasta padrão
WORKDIR /home/nodejs/app

# Evitar interação durante instalação dos pacotes
ENV DEBIAN_FRONTEND=noninteractive

# Define variáveis de ambiente
ENV FIREBASE_APIKEY ${{ secrets.FIREBASE_APIKEY }}
ENV FIREBASE_MSENDERID ${{ secrets.FIREBASE_MSENDERID }}
ENV FIREBASE_APPID ${{ secrets.FIREBASE_APPID }}
ENV FIREBASE_MID ${{ secrets.FIREBASE_MID }}
ENV MSAL_CLIENT_ID ${{ secrets.MSAL_CLIENT_ID }}
ENV MSAL_REDIRECT_URI ${{ secrets.MSAL_REDIRECT_URI }}
ENV ONEDRIVE_URI ${{ secrets.ONEDRIVE_URI }}
ENV NODE_ENV production

# Instala o node 12
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt -y install nodejs gcc g++ make

# Adiciona novo usuário e grupo para evitar usar o root
RUN groupadd -r nodejs && useradd -m -r -g nodejs -s /bin/bash nodejs

# Copia package.json e instala dependências criando um layer(cache) para ele
COPY package.json .
RUN npm install

# Adicionar arquivos do repositório no container
COPY . .

# Corrige permissões da pasta
RUN chmod -Rf 775 /home/nodejs && chown -Rf nodejs:nodejs /home/nodejs

# Passa a usar o novo usuário não root "nodejs"
USER nodejs

# Expor porta 3000
# TODO: Testar variavél de ambiente de porta e selecionar ela caso definida
EXPOSE 3000

# Roda servidor ao dar run na imagem.
CMD ["npm", "run", "start"]