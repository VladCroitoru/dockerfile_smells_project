FROM 	stakater/base-alpine:3.5
LABEL	authors="Rasheed <rasheed@aurorasolutions.io>"

ADD start.sh /start.sh
RUN chmod +x /start.sh

VOLUME ["/shared"]

CMD [ "/start.sh" ]