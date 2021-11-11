FROM movecrew/one4ubot:alpine-latest

RUN git clone -b sql-extended https://github.com/vaibhavchandra13/GenBot /root/GenBot
RUN chmod 777 /root/GenBot
WORKDIR /root/GenBot/

EXPOSE 80 443

CMD ["python3","-m","GenBot"]
