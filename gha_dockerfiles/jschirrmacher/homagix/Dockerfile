FROM node:14-alpine@sha256:c346198378f78f8611254dce222e7e6635804e41e5203d1825321edd6c59dca1 as builder
WORKDIR /build
ADD . .
RUN npm ci && \
    npm run build && \
    rm -rf node_modules && \
    npm ci --production && \
    mkdir /app && \
    mv build/server build/frontend node_modules package.json public /app


FROM node:14-alpine@sha256:c346198378f78f8611254dce222e7e6635804e41e5203d1825321edd6c59dca1
ENV NODE_ENV production
WORKDIR /app
COPY --from=builder /app .
RUN chown -R node.node .
USER node


EXPOSE 8200
ENV NODE_ENV production
ENV BASEDIR /app
CMD node server
