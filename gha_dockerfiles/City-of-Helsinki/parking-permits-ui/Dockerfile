# ===============================================
FROM node:14-slim as appbase
# ===============================================

# Yarn
ENV YARN_VERSION 1.22.10
RUN yarn policies set-version $YARN_VERSION

WORKDIR /app

# Copy package.json and package-lock.json/yarn.lock files
COPY package*.json *yarn* ./

# Install dependencies
RUN yarn install


# =============================
FROM appbase as development
# =============================
# Copy all files
COPY . .
CMD ["yarn", "start"]


#==============================
FROM appbase as staticbuilder
#==============================
COPY . /app
RUN yarn build


# ============================================================
FROM registry.access.redhat.com/ubi8/nginx-118 as production
# =============================================================
# Copy static build
COPY --from=staticbuilder /app/build /usr/share/nginx/html

# Copy nginx config
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]
