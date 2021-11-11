FROM python:2.7
# Setup useful environment variables

WORKDIR /home/pancake
COPY . .
RUN chmod +x configure.sh
USER root
CMD ["/home/pancake/configure.sh"]