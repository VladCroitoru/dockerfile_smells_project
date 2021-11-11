FROM uselessregistry.azurecr.io/react-base
COPY src/ /usr/app/src/
COPY public/ /usr/app/public/
RUN npm run build
CMD serve -s build
