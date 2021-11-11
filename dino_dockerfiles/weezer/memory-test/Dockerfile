FROM nginx
RUN apt-get update && apt-get install -y --force-yes stress
EXPOSE 80
COPY ./start.sh .
RUN chmod +x ./start.sh
ENTRYPOINT ["./start.sh"]
