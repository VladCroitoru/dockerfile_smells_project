FROM eyedeekay/plexurl:deps
USER root
COPY . /home/plexurl/plexurl/
WORKDIR /home/plexurl/plexurl
RUN pip3 install --exists-action w -e .
USER plexurl
ENTRYPOINT [ "sh", "-i", "-c" ]
