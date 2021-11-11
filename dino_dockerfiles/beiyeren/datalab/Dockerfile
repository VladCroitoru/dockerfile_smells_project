#
FROM gcr.io/cloud-datalab/datalab:local-20180214
RUN pip  --no-cache-dir install keras tflearn prettytensor tensorflow-transform h5py && pip3 --no-cache-dir install keras tflearn prettytensor h5py
ENV ENABLE_USAGE_REPORTING=false
WORKDIR /
CMD mkdir /root/.ipython/profile_default
COPY ipython_config.py /root/.ipython/profile_default/
COPY run.sh /datalab/run.sh
ENTRYPOINT ["/datalab/run.sh"]
