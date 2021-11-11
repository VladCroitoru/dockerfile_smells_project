FROM thraxil/django.base:2020-09-26-83678bbd1abe
COPY package.json /node/
RUN cd /node && npm set progress=false && npm install && touch /node/node_modules/sentinal
COPY requirements.txt /app/requirements.txt
RUN /ve/bin/pip3 install -r /app/requirements.txt && touch /ve/sentinal
WORKDIR /app
COPY . /app/
RUN VE=/ve/ MANAGE="/ve/bin/python3 manage.py" NODE_MODULES=/node/node_modules make all
EXPOSE 8000
ENV APP mithras
ENTRYPOINT ["/run.sh"]
CMD ["run"]
