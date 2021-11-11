FROM almir/webhook
MAINTAINER Sean Payne <spayne@seanpayne.name>

# Make sure to specify the IFTTT Maker key on the 'docker run' commandline.
ENV IFTTT_MAKER_KEY=KEY_NOT_SET

RUN apk add --update jq curl

ADD hooks.json /etc/webhook/hooks.json
ADD ifttt-maker-post.sh /var/scripts/ifttt-maker-post.sh

CMD ["-verbose","-hooks=/etc/webhook/hooks.json"]
