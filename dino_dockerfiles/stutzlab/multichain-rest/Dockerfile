#FROM node:8.6.0
FROM node:9.4-alpine
ENV work_dir /app

WORKDIR ${work_dir}

ADD src/package.json ${work_dir}
RUN npm install

ADD src/ ${work_dir}

ENV MULTICHAIN_HOST localhost
ENV MULTICHAIN_PORT 8000
ENV MULTICHAIN_USER multichainrpc
ENV MULTICHAIN_PASS 0000

EXPOSE 8000
CMD ["npm", "start"]
