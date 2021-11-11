FROM grahamdumpleton/warp0-debian8-python27

# We need to extend the image so we have to be root.

USER root

# Install any additional system packages. These are required by Jupyter
# notebook or various modules for data analysis and visualisation.

RUN apt-get update && apt-get install -y libfreetype6 libfreetype6-dev \
    libpng++ libpng++-dev liblapack-dev libatlas-dev gfortran \
    libav-tools libgeos-dev && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

# Copy in S2I scripts and override S2I labels to flag this as now being
# builder for Jupyter notebooks.

COPY s2i ${WARPDRIVE_APP_ROOT}/.s2i
COPY run.sh ${WARPDRIVE_APP_ROOT}/run.sh

COPY requirements.txt ${WARPDRIVE_SRC_ROOT}/requirements.txt

RUN chown 1001:0 ${WARPDRIVE_SRC_ROOT}/requirements.txt

LABEL io.k8s.description="S2I builder for Jupyter Notebooks (Python 2.7)." \
      io.k8s.display-name="Jupyter Notebook (Python 2.7)" \
      io.openshift.tags="builder,python,python27,jupyter"

# Switch back to non 'root' user. Must use the uid and not the user name
# else will be rejected by 's2i' under OpenShift as can't know whether
# is pretending to be a non 'root' user.

USER 1001

# Install packages required for Jupyter notebook and ipyparallel.

RUN warpdrive build && \
    rm ${WARPDRIVE_SRC_ROOT}/requirements.txt && \
    chmod -Rf g+w ${WARPDRIVE_APP_ROOT} || true

# Expose ports needed when running a parallel compute cluster using the
# ipyparallel module.

EXPOSE 10000-10011

# Override 'CMD' so we can wrap the startup of Jupyter notebook or switch
# it out and instead run 'ipengine' or 'ipcontroller' when running a
# parallel compute cluster.

CMD [ "/opt/app-root/s2i/bin/run" ]
