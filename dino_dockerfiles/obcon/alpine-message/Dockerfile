FROM obcon/alpine-worker

USER root
ADD worker /home/worker
RUN npm install && chown -R worker:worker /home/worker
USER worker
ENV RABBITMQ 127.0.0.1
