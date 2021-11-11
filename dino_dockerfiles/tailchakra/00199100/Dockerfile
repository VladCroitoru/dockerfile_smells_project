FROM mkenney/npm:alpine
EXPOSE 1730
RUN git clone https://github.com/Deezloader/DeezLoader-Reborn DeezLoader-Reborn \
    && mv DeezLoader-Reborn/app / \
    && rm -R DeezLoader-Reborn
WORKDIR /app
RUN ["npm", "install"]
CMD ["node", "app.js"]
VOLUME ["/downloads"]
