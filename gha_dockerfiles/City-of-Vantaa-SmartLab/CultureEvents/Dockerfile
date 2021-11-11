FROM node:8.10
WORKDIR /backend
ADD ./backend /backend
RUN npm install
ADD ./frontend /frontend
WORKDIR /frontend
RUN npm install
RUN npm run build
RUN cp -r ./build ../backend/public
WORKDIR /backend
EXPOSE 3000
CMD ["npm", "run", "start:prod"]