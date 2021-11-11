FROM node:14 as builder
WORKDIR /workspace
COPY . .
RUN npm install

FROM node:14-alpine
WORKDIR /workspace
COPY --from=builder /workspace .
CMD npm start
EXPOSE 3002
