FROM project8/cvmfs-dependencies-common:build-2017-10-18

ENV P8DEPMORPHOBUILD=build-2017-10-18

RUN mkdir -p /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}

ADD ./setup.sh /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/setup.sh
ADD ./dependency_urls.txt /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/dependency_urls.txt
ADD ./download_pkg.sh /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/download_pkg.sh
ADD ./install.sh /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/install.sh
ADD ./python_tester.py /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/python_tester.py

RUN source /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/setup.sh && \
    chmod +x /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/download_pkg.sh &&\    
    sleep 1 &&\
    /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/download_pkg.sh && \
    chmod +x /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/install.sh &&\    
    sleep 1 &&\
    /cvmfs/hep.pnnl.gov/project8/dependencies-morpho/${P8DEPMORPHOBUILD}/install.sh
