FROM node AS translations-handler

RUN mkdir -p /opt/translations/dist
WORKDIR /opt/translations

RUN git init
RUN git remote add origin https://github.com/hzi-braunschweig/SORMAS-Project.git
RUN git fetch
RUN git checkout origin/development sormas-api/src/main/resources/

COPY docker/translations/convertTranslations.ts /opt/translations
COPY docker/translations/package.json /opt/translations
COPY docker/translations/package-lock.json /opt/translations
COPY src/assets/i18n/custom-translations.json /opt/translations

RUN cp -rf sormas-api/src/main/resources/* ./

RUN npm ci
RUN npx ts-node convertTranslations.ts

FROM node AS compile-image

WORKDIR /opt/ng
COPY package.json package-lock.json ./
RUN npm install

ENV PATH="./node_modules/.bin:$PATH"

COPY . ./
RUN npm run build

FROM nginx
COPY docker/angular/nginx.conf /etc/nginx/nginx.conf
COPY docker/angular/configure-envionment.sh /docker-entrypoint.d/99-configure-envionment.sh

COPY --from=compile-image /opt/ng/dist/app /usr/share/nginx/html
