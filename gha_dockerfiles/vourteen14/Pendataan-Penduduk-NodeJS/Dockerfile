FROM node:14.17.6
ENV DB_HOST='mongodb+srv://anggasuriana:Ex9ZeI9aRyF7CDi9@cluster0.o7wse.mongodb.net/Penduduk?retryWrites=true&w=majority'
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
CMD npm run dev
EXPOSE 6969
