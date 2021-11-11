FROM maprox/base

RUN git clone https://github.com/maprox/Pipe.git /pipe

WORKDIR /pipe

RUN pip3 install -r requirements.txt --upgrade

ENV PIPE_ENVIRONMENT="production" \
    PIPE_HOSTNAME="trx.maprox.net" \
    PIPE_HOSTIP="212.100.159.142" \
    PIPE_HANDLER="" \
    PIPE_PORT="20000" \
    PIPE_LOGSPATH="/pipe/logs" \
    REDIS_PORT="6379" \
    REDIS_HOST="127.0.0.1" \
    REDIS_PASS="" \
    AMQP_CONNECTION="amqp://guest:guest@127.0.0.1//"

ENTRYPOINT ["python3", "main.py"]

CMD ["-l", "stdout"]