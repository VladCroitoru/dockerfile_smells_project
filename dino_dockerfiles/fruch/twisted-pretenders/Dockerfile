FROM pretenders/pretenders:1.4

MAINTAINER israel.fruchter@gmail.com

ENV PYTHONPATH=/opt/pretenders
ENV PKGS='alpine-sdk python3-dev'

RUN\
     # Install packages
     apk update  &&\
     apk add $PKGS  &&\

     pip3 install twisted &&\
     pip3 install -r /opt/pretenders/requirements/runtime.txt &&\

     # cleanup
     apk del $PKGS  &&\
     rm -rf /var/cache/apk/* /root/.cache /tmp/*


RUN sed 's/bottle.run(app=pretender_app/bottle.run(server="twisted", app=pretender_app/' -i /opt/pretenders/pretenders/server/server.py

CMD ["python3", "-m", "pretenders.server.server", "--host", "0.0.0.0", "--port", "8000"]

