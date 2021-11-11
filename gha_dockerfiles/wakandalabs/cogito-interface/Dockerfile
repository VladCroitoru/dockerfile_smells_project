FROM nginx:alpine
# run ```yarn build``` first
COPY ./build /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]