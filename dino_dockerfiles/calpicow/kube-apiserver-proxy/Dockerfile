FROM nginx:stable

COPY v3.ext /etc/nginx/
COPY nginx.conf /etc/nginx/

CMD ["/bin/sh", "-c", "cp /mnt/* /dev/shm/ && openssl genrsa -out /dev/shm/tls-key.pem 2048 && openssl req -new -key /dev/shm/tls-key.pem -out /dev/shm/tls.csr -subj /CN=minikube && openssl x509 -req -CA /dev/shm/ca.crt -CAkey /dev/shm/ca.key -CAcreateserial -extfile /etc/nginx/v3.ext -in /dev/shm/tls.csr -out /dev/shm/tls.pem && exec nginx -g 'daemon off;'"]
