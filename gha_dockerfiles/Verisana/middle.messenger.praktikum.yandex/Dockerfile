FROM node:14-bullseye AS appBuild

ENV USERNAME user
ENV APPDIR app
ENV HOMEDIR /home/${USERNAME}/
WORKDIR ${HOMEDIR}${APPDIR}

RUN apt-get update && apt-get install -y npm

COPY --chown=${USER} ./package-lock.json .
COPY --chown=${USER} ./package.json .
RUN npm ci
COPY --chown=${USER} . .

RUN npm run build

FROM node:14-bullseye

ENV USERNAME user
ENV APPDIR app
ENV HOMEDIR /home/${USERNAME}/
ENV TZ Asia/Yekaterinburg

RUN useradd --create-home ${USERNAME} && chown -R ${USERNAME} /home/${USERNAME}/
WORKDIR ${HOMEDIR}${APPDIR}

RUN apt-get update && apt-get -y install netcat locales nano apt-utils npm

# Locale
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
  && locale-gen

ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

# +Timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY --chown=${USER} ./package-lock.json .
COPY --chown=${USER} ./package.json .
RUN npm ci --production
COPY --chown=${USER} --from=appBuild ${HOMEDIR}${APPDIR}/dist ./dist
COPY --chown=${USER} ./src/server.ts ./src/server.ts
COPY --chown=${USER} ./tsconfig.json ./tsconfig.ts

USER ${USER}

CMD ["npm", "run", "start"]
