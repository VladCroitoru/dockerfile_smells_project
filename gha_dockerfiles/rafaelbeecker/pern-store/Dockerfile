FROM node:14.16-alpine

WORKDIR /usr/app

COPY ./backend/package.json backend/package.json
COPY ./backend/package-lock.json backend/package-lock.json
RUN (cd backend; npm install --production)
COPY ./backend backend/

COPY ./frontend/package.json frontend/package.json
COPY ./frontend/yarn.lock frontend/yarn.lock
RUN (cd /usr/app/frontend; yarn)
COPY ./frontend frontend/
RUN (cd frontend; yarn build)

EXPOSE 8080

WORKDIR /usr/app/backend

ENV NODE_ENV=production
CMD ["node", "index.js"]