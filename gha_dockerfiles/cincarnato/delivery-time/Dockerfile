#BULDER
FROM node:12.16.1-alpine3.9 as builder

#BACKEND Dependencies
COPY ./apps/backend/package.json /workspace/backend/package.json
COPY ./apps/backend/package-lock.json /workspace/backend/package-lock.json

WORKDIR /workspace/backend
RUN npm install


#FRONTEND Dependencies
COPY ./apps/frontend/package.json /workspace/frontend/package.json
COPY ./apps/frontend/package-lock.json /workspace/frontend/package-lock.json

WORKDIR /workspace/frontend
RUN npm install

#CP APPs BACKEND & FRONTEND
COPY ./apps /workspace

#BACKEND BUILD
WORKDIR /workspace/backend
RUN npm run build

#FRONTEND BUILD
WORKDIR /workspace/frontend
RUN npm run build

#RUNNER
FROM node:12.16.1-alpine3.9

RUN apk add bash
RUN npm install pm2 -g

COPY --from=builder /workspace/backend/dist /app
COPY --from=builder /workspace/frontend/dist /app/web

WORKDIR /app
RUN npm install --only=production

ENTRYPOINT ["pm2-runtime", "start", "index.js", "--name", "dracul-scaffold"]
