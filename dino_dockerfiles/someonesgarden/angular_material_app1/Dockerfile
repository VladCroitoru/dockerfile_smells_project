FROM someonesgarden/angular_material_base:latest

COPY node_modules /node_modules/
COPY public /usr/src/app/public/
COPY views /usr/src/app/views/

EXPOSE 8080

CMD [ "coffee", "bin/www.coffee" ]

