FROM nginx:1.17.4

RUN apt-get update
RUN apt-get -y install wget
RUN apt-get -y install dos2unix
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN chmod 755 Miniconda3-latest-Linux-x86_64.sh
RUN ./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda3
RUN rm Miniconda3-latest-Linux-x86_64.sh
RUN /miniconda3/bin/conda create -n trails-viz-api python=3.7 -y
ENV PATH /miniconda3/envs/trails-viz-api/bin:$PATH

RUN /miniconda3/bin/conda install --name trails-viz-api uwsgi -c defaults -c conda-forge -y

COPY docker-conf/nginx.conf /etc/nginx/nginx.conf
COPY docker-conf/default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /app/logs

COPY trails-viz-app/dist /usr/share/nginx/html
COPY trails-viz-api/uwsgi-config.ini /app/uwsgi-config.ini
COPY docker-conf/start.sh /app/start.sh

COPY trails-viz-api/dist/trailsvizapi-*-py3-none-any.whl /app/

RUN dos2unix /app/start.sh
RUN chmod 755 /app/start.sh
RUN cd /app && whl_file=`ls | grep whl` && /miniconda3/envs/trails-viz-api/bin/pip install $whl_file && cd ..

WORKDIR /app

EXPOSE 80 443

CMD ["/bin/bash", "./start.sh"]
