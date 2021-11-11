#FROM is the base image for which we will run our application
FROM nginx:latest

# Copy files and directories from the application
COPY index.html /usr/share/nginx/html
COPY pictures.html /usr/share/nginx/html
COPY story.html /usr/share/nginx/html
COPY videos.html /usr/share/nginx/html
COPY style.css /usr/share/nginx/html
COPY images/ /usr/share/nginx/html/images/

# Tell Docker we are going to use this port
EXPOSE 80