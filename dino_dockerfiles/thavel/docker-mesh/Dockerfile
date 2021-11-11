FROM alpine:3.3

RUN apk add --update bash python3 python3-dev make gcc libc-dev git && rm -rf /var/cache/apk/*
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN curl https://bootstrap.pypa.io/get-pip.py | python

WORKDIR /home/
COPY ./ ./
RUN pip install -r requirements.txt

EXPOSE 80
EXPOSE 8080
ENTRYPOINT [ "python", "mesh.py" ]
