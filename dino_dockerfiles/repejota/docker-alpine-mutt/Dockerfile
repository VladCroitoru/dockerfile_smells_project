FROM alpine:edge
LABEL maintainer Raül Perez <repejota@gmail.com>

RUN addgroup -g 1000 user \
    && adduser -D -h /home/user -G user -u 1000 user

RUN apk --no-cache add \
	ca-certificates \
	elinks \
	git \
	gnupg1 \
	links \
	mutt \
	mutt-doc \
	vim

ENV BROWSER links

USER user
ENV HOME /home/user
ENV TERM xterm-256color
RUN mkdir -p $HOME/.mutt/cache/headers $HOME/.mutt/cache/bodies \
	&& touch $HOME/.mutt/certificates

ENV LANG C.UTF-8

COPY entrypoint.sh /entrypoint.sh
COPY .mutt $HOME/.mutt

ENTRYPOINT ["/entrypoint.sh"]

CMD ["mutt", "-F", "~/.mutt/muttrc"]
