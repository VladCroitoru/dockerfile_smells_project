version: "2"
services:
  node:
    image: "node:8"
    user: "node"
    working_dir: /home/fluffle/code/Marking/
    environment:
      - NODE_ENV=production
    volumes:
      - ./:/home/fluffle/code/Marking/
    expose:
      - "8081"
    command: "npm start"