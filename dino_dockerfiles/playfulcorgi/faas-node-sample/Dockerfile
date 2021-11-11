FROM playfulcorgi/faas-node
COPY . ./
RUN npm i
ENV HANDLER_FILE_SUBPATH="dist/index.js"
CMD ["npm", "run", "watch"]