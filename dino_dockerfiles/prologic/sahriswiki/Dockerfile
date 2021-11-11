FROM prologic/python-runtime:2.7

ENTRYPOINT ["sahriswiki"]
CMD ["-p", "80", "--debug"]

EXPOSE 80

VOLUME /data

RUN apk -U add build-base python-dev git && \
    rm -rf /var/cache/apk/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

WORKDIR /app
COPY . /app/
RUN pip install .
