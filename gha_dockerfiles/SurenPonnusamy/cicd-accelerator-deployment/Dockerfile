FROM ubuntu:latest

ADD supervisord.conf /etc/supervisord.conf

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install nodejs npm curl supervisor -y

ADD cicd-accelerator-frontend cicd-accelerator-frontend

ADD cicd-accelerator-backend cicd-accelerator-backend

EXPOSE 3001 3000

CMD ["supervisord", "-c", "/etc/supervisord.conf"]