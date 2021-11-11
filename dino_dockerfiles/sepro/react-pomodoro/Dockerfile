# Build docker file
# docker build -t CONTAINERNAME .

# Run container 
# docker run -p 80:80 -d CONTAINERNAME


FROM kyma/docker-nginx

COPY dist/ /var/www

CMD 'nginx'
