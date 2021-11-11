FROM node:14 as frontend
WORKDIR /usr/src/app
COPY frontend/package.json .
RUN npm i
COPY frontend/ .
RUN npm run build


FROM nginx:1.21.1
WORKDIR /usr/src/app
COPY --from=frontend /usr/src/app/dist ./frontend
RUN apt-get update && apt install -y redis-server && apt-get install -y python3-pip && python3.7 -m pip install --upgrade pip && apt-get install -y ffmpeg
WORKDIR /usr/src/app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend .
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 48763
CMD python3 manage.py migrate && ./Run.sh && service redis-server restart && nginx -g 'daemon off;'
