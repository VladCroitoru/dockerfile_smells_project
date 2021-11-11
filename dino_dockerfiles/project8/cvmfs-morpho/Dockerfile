FROM project8/cvmfs-dependencies-morpho:build-2017-10-18

ENV MORPHOBRANCH=v1.4.1

RUN git clone https://github.com/project8/morpho.git /cvmfs/hep.pnnl.gov/project8/morpho/${MORPHOBRANCH} --recursive -b ${MORPHOBRANCH}

ADD ./setup.sh /cvmfs/hep.pnnl.gov/project8/morpho/${MORPHOBRANCH}/setup.sh
ADD ./install.sh /cvmfs/hep.pnnl.gov/project8/morpho/${MORPHOBRANCH}/install.sh

## Installing morpho ##
RUN chmod +x /cvmfs/hep.pnnl.gov/project8/morpho/${MORPHOBRANCH}/setup.sh && \
    sleep 1 && \
    /cvmfs/hep.pnnl.gov/project8/morpho/${MORPHOBRANCH}/setup.sh && \
    chmod +x /cvmfs/hep.pnnl.gov/project8/morpho/${MORPHOBRANCH}/install.sh && \
    sleep 1 && \
    /cvmfs/hep.pnnl.gov/project8/morpho/${MORPHOBRANCH}/install.sh
