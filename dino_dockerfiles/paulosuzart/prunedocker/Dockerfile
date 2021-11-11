FROM jackfirth/racket

RUN mkdir /app
WORKDIR /app
COPY prunedocker.rkt prunedocker.rkt
RUN ls -lah /app

ENTRYPOINT ["racket", "prunedocker.rkt"]

