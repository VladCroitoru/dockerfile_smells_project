FROM alpine:edge
RUN apk add --update --progress \
        musl \
        build-base \
        python3 \
        python3-dev \
        bash \
        git \
        curl \
        busybox \
      #  busybox-extras \
    && pip3 install --no-cache-dir --upgrade pip

RUN cd /usr/bin \
    && ln -sf python3 python \
    && ln -sf pip3 pip

# COPY entrypoint.sh /opt/entrypoint.sh
COPY requirements.txt /opt/requirements.txt
COPY app.py /opt/app.py
# RUN  chmod 777 /opt/entrypoint.sh
RUN pip install -r /opt/requirements.txt  
# ENTRYPOINT ["/opt/entrypoint.sh" ]
ENTRYPOINT ["python" ]
EXPOSE 80
# CMD ["a" , "b" , "c" , "d" , "e" ]  
CMD ["/opt/app.py"]
