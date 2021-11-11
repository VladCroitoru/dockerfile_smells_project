FROM alpine:3.6

ENV HOME /quimby

WORKDIR $HOME

RUN apk -U add python3 && \
    rm /var/cache/apk/* && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip --no-cache-dir && \
    adduser -D -h $HOME -s /sbin/nologin quimby

COPY requirements.txt $HOME/

RUN pip3 install --no-cache-dir -r requirements.txt

USER quimby

COPY . $HOME/

EXPOSE 5000

CMD ["python3", "app.py"]
