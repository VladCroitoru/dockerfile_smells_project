FROM radanalyticsio/base-notebook

USER root
RUN mkdir /data

ENV NB_USER=nbuser
ENV NB_UID=1011

EXPOSE 8888

USER $NB_UID

ADD wikieod.parquet /data/wikieod.parquet
ADD msgs.parquet /data/msgs.parquet

ADD var.ipynb /notebooks/var.ipynb
ADD pyspark.ipynb /notebooks/pyspark.ipynb
ADD ml-basics.ipynb /notebooks/ml-basics.ipynb
ADD auto-mpg.json /notebooks/data/

USER root

RUN chown -R $NB_USER:root /home/$NB_USER /data \
    && find /home/$NB_USER -type d -exec chmod g+rwx,o+rx {} \; \
    && find /home/$NB_USER -type f -exec chmod g+rw {} \; \
    && find /data -type d -exec chmod g+rwx,o+rx {} \; \
    && find /data -type f -exec chmod g+rw {} \; \
    && chmod -f g+rw /notebooks/*

USER $NB_UID
ENV HOME /home/$NB_USER

LABEL io.k8s.description="PySpark Jupyter Notebook with VaR calculation." \
      io.k8s.display-name="PySpark Jupyter Notebook with VaR calculation." \
      io.openshift.expose-services="8888:http"

CMD ["/entrypoint", "/start.sh"]
