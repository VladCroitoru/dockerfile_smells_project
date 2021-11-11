FROM node:6-onbuild

EXPOSE 4200

## Mark as a production angular app
RUN sed -i "/@NgModule/i\
import { enableProdMode } from '@angular/core';\n\
enableProdMode();\n\
" src/app/app.module.ts

RUN npm install

CMD ["npm", "start"]
