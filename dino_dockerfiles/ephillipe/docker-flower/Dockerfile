FROM      python:2.7

# WARNING: BE SURE NOT TO USE THE WORD 'FLOWER' IN THE ENV VARS
# E.G. VIA LINKING OR MAESTRO-NG: THEY HAVE A SPECIAL MEANING IN FLOWER.

RUN pip install redis \
    && pip install https://github.com/mher/flower/zipball/master  

ENV TZ=America/Sao_Paulo
RUN rm -vf /etc/localtime \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  \
    && echo $TZ > /etc/timezone

# Default port
EXPOSE    5555

CMD flower --broker=$BROKER_URL
