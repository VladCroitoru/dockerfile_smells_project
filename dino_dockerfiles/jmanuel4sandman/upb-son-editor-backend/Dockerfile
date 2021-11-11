FROM tiangolo/uwsgi-nginx-flask:flask-python3.5

#install son-cli tools
RUN pip install git+https://github.com/sonata-nfv/son-cli

#install son-editor-backend
RUN mkdir -p /root/son-editor/workspaces
COPY . /app
COPY ./no-ssl-nginx.conf /etc/nginx/conf.d/nginx.conf

# Set the default directory where CMD will execute
WORKDIR /app

#set git a dummy user to be enable stashing the config file
RUN git config user.email "dummy@user.com"
RUN git config user.name "Dummy User"

#install the son-editor requirements
RUN pip install -e .

#expose ports
#son-editor-backend
EXPOSE 5000
#github-webhook
EXPOSE 5050

#make sure entrypoint is executable
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
