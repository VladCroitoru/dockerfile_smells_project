FROM node:17-alpine as builder

# Configuration
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL ${REACT_APP_API_URL:-http://localhost:4070}

ARG REACT_APP_GOOGLE_RECAPTCHA_SITEKEY
ENV REACT_APP_GOOGLE_RECAPTCHA_SITEKEY ${REACT_APP_GOOGLE_RECAPTCHA_SITEKEY:-secretKey}

ARG REACT_REFRESH_TIME
ENV REACT_REFRESH_TIME ${REACT_REFRESH_TIME:-180}

# Build project
WORKDIR /src
COPY ./ ./
RUN npm i --ignore-scripts
RUN npm run build

FROM nginx:1.21.3-alpine
WORKDIR /usr/share/nginx/html
COPY --from=builder /src/build ./
