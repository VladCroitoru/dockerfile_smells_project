FROM debian:stretch

LABEL maintainer Vincent RAVERA <ravera.vincent@gmail.com>

RUN apt-get update
RUN apt-get install jupyter-notebook -y
# Extra
RUN apt-get install jupyter-nbextension-jupyter-js-widgets -y

WORKDIR /home/

EXPOSE 8888

CMD jupyter-notebook --ip="0.0.0.0"
