ARG base
FROM ghcr.io/anyakichi/yocto-builder:${base}

ARG yocto_branch
COPY ${yocto_branch}/buildenv.d/* /etc/buildenv.d/

ARG yocto_machine="ek874|hihope-rzg2{h,m,n}"
ARG meta_rzg2_branch="master"
ENV \
  YOCTO_MACHINE=${yocto_machine} \
  YOCTO_BITBAKE_TARGET=core-image-weston \
  META_RZG2_BRANCH=${meta_rzg2_branch}
