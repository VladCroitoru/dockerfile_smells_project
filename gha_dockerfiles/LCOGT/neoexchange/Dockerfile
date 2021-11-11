################################################################################
# Findorb Builder Container
################################################################################
FROM centos:8 AS findorbbuilder

# Choose specific release versions of each piece of software
ENV LUNAR_VERSION=016b82f80bd509929e0d55136ed6882e61831dfb \
    JPL_EPH_VERSION=d460e8ace0e5d3036e29838444b4f3fee85f0a45 \
    SAT_CODE_VERSION=603b744c10ad37e9bdbd2cd328d214375446b044 \
    FIND_ORB_VERSION=e45ba9f0b92eb783848711d69c33e20c607124d4

# This software requires GCC >= 7.0 to build
RUN yum -y install gcc gcc-c++ make git ncurses-devel \
        && yum -y clean all

# Build "lunar". No need to clean up, as this is a builder container.
# The contents will be discarded from the final image.
RUN curl -fsSL https://github.com/Bill-Gray/lunar/archive/${LUNAR_VERSION}.tar.gz | tar xzf - \
        && cd lunar-${LUNAR_VERSION} \
        && make \
        && make install

# Build "jpl_eph". No need to clean up, as this is a builder container.
# The contents will be discarded from the final image.
RUN curl -fsSL https://github.com/Bill-Gray/jpl_eph/archive/${JPL_EPH_VERSION}.tar.gz | tar xzf - \
        && cd jpl_eph-${JPL_EPH_VERSION} \
        && make \
        && make install

# Compile "integrat" (a part of "lunar" which has a dependency on "jpl_eph",
# which itself has a dependency on "lunar". Circular dependencies are fun, huh?)
RUN cd lunar-${LUNAR_VERSION} \
        && make integrat \
        && make install_integrat

# Build "sat_code". No need to clean up, as this is a builder container.
# The contents will be discarded from the final image.
RUN curl -fsSL https://github.com/Bill-Gray/sat_code/archive/${SAT_CODE_VERSION}.tar.gz | tar xzf - \
        && cd sat_code-${SAT_CODE_VERSION} \
        && make \
        && make install

# Build "find_orb". No need to clean up, as this is a builder container.
# The contents will be discarded from the final image.
RUN curl -fsSL https://github.com/Bill-Gray/find_orb/archive/${FIND_ORB_VERSION}.tar.gz | tar xzf - \
        && cd find_orb-${FIND_ORB_VERSION} \
        && make \
        && make install \
        && curl -fsSL https://www.minorplanetcenter.net/iau/lists/ObsCodes.html > /root/.find_orb/ObsCodes.htm \
        && if [[ -f "ps_1996.dat" && -f "elp82.dat" ]]; then cp ps_1996.dat elp82.dat /root/.find_orb; fi

# Copy default findorb config file
COPY neoexchange/photometrics/configs/environ.def /root/.find_orb/

################################################################################
# damit Builder Container
################################################################################
FROM centos:8 AS damitbuilder

# Choose specific release versions of each piece of software
ENV DAMIT_VERSION="version_0.2.1"

# This software requires GCC and gfortran to build
RUN yum -y install gcc gcc-gfortran make  \
        && yum -y clean all

# Build all of damit's components. No need to clean up, as this is a builder container.
# The contents will be discarded from the final image.
RUN curl -fsSL https://astro.troja.mff.cuni.cz/projects/damit/files/${DAMIT_VERSION}.tar.gz | tar xzf - \
        && cd ${DAMIT_VERSION} \
        && cd convexinv \
        && make \
        && cd ../conjgradinv \
        && make \
        && cd ../lcgenerator \
        && make \
        && cd ../fortran \
        && gfortran -o minkowski minkowski.f \
        && gfortran -o standardtri standardtri.f \
        && cd ..

# copy binaries
RUN cd ${DAMIT_VERSION} \
        && if [[ -f "convexinv/convexinv" ]]; then cp convexinv/convexinv /usr/local/bin; fi \
        && if [[ -f "conjgradinv/conjgradinv" && -f "lcgenerator/lcgenerator" ]]; then cp conjgradinv/conjgradinv /usr/local/bin; fi \
        && if [[ -f "lcgenerator/lcgenerator" ]]; then cp lcgenerator/lcgenerator /usr/local/bin; fi \
        && if [[ -f "fortran/minkowski" && -f "fortran/standardtri" ]]; then cp fortran/{minkowski,standardtri} /usr/local/bin; fi


################################################################################
# Production Container
################################################################################
FROM centos:8

# Copy findorb from builder container
COPY --from=findorbbuilder /root /root
# Copy damit binaries from builder container
COPY --from=damitbuilder /usr/local/bin /root/bin

# Install Python dependencies

# Add LCO RPM repository
COPY docker/etc/yum.repos.d/lcogt.repo /etc/yum.repos.d/lcogt.repo

# Install build dependencies for Python packages
# XXX Need to install powertools repo
# 'glibc-langpack-en' is needed to prevent locale complaints (https://www.tecmint.com/fix-failed-to-set-locale-defaulting-to-c-utf-8-in-centos/)
RUN yum -y install epel-release glibc-langpack-en\
        && yum -y install \
            gcc \
            gcc-c++ \
            gcc-gfortran \
            python36 \
            python36-devel \
            libffi-devel \
            libjpeg-devel \
            libpng-devel \
            mariadb-devel \
            make diffutils file

# Copy Python dependencies manifest
COPY neoexchange/requirements.txt .

# Install the LCO NEO exchange Python required packages
# Upgrade pip first
# Then the LCO packages which have to be installed after the normal pip install
# numpy needs to be explicitly installed first otherwise pySLALIB fails with a
# missing numpy.distutils.core reference because the package's setup.py is broken
RUN pip3 --no-cache-dir install --upgrade pip \
    && python3 -m pip --no-cache-dir install --upgrade numpy wheel \
    && python3 -m pip --no-cache-dir install --trusted-host buildsba.lco.gtn -r requirements.txt

# Add path to findorb
ENV PATH=/root/bin:$PATH

# The entry point is our init script, which runs startup tasks, then starts gunicorn
ENTRYPOINT [ "/init" ]

# Supercronic environment variables
ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.9/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=5ddf8ea26b56d4a7ff6faecdd8966610d5cb9d85

# Supercronic installation
RUN curl -fsSLO "$SUPERCRONIC_URL" \
        && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
        && chmod +x "$SUPERCRONIC" \
        && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
        && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

# Install Node.JS
RUN dnf -y module install nodejs:14

# Install packages and update base system
# XXX Need to install powertools repo
RUN yum -y install \
            cdsclient \
            ImageMagick \
            less \
            mtdlink \
            plplot \
            scamp \
            sextractor \
            tcsh \
            wget \
            which \
        && yum -y clean all

# Copy operating system configuration files
COPY docker/ /

# Set working directory
WORKDIR /var/www/apps/neoexchange

# Copy web application into working directory
COPY neoexchange .
