#####
## Docker image for the STAC UI
#####

ARG BASE_IMAGES_REGISTRY=registry.ceda.ac.uk/base-images
ARG BASE_IMAGES_VERSION

ARG GIT_REPOSITORY=https://github.com/cedadev/stac-ui.git
ARG GIT_VERSION=715fad315cad06d5d828a23f61203e5064b3e214

FROM ${BASE_IMAGES_REGISTRY}/git-checkout:${BASE_IMAGES_VERSION} as application-source

FROM ${BASE_IMAGES_REGISTRY}/js-build:${BASE_IMAGES_VERSION} as js-build
# Link the build directory to dist as expected by js-serve
RUN ln -s /application/build /application/dist

FROM ${BASE_IMAGES_REGISTRY}/js-serve:${BASE_IMAGES_VERSION}
