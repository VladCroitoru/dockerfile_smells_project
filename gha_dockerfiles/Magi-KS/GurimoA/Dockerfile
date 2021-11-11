################################################################################
# BUILD STAGE
################################################################################

FROM node:lts-bullseye-slim AS builder

WORKDIR /build
RUN npm install --global npm
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential python3

COPY . .
RUN npm install
RUN npm run build-custom-parcel
RUN npm run build

################################################################################
# RUNTIME STAGE
################################################################################
FROM nginx:alpine AS nginx

COPY nginx.conf /etc/nginx/nginx.conf
WORKDIR /gurimoa
COPY --from=builder /build/dist .
