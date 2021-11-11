FROM alpine:3.3

RUN apk add --no-cache python3
RUN python3 -m ensurepip
RUN rm -r /usr/lib/python*/ensurepip
RUN pip3 install --upgrade pip setuptools
COPY pip_requierement /tmp/pip_requierement
RUN pip3 install --upgrade -r /tmp/pip_requierement
RUN rm -r /root/.cache
	
CMD /bin/sh