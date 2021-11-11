FROM norionomura/sourcekit:311

# Environment Variables

ENV SWIFTLINT_TAG="0.20.1" \
    SWIFTLINT_BUILD_DIR="/swiftlint_build" \
    LINT_WORK_DIR="/project"

WORKDIR "${SWIFTLINT_BUILD_DIR}"

RUN git clone https://github.com/realm/SwiftLint.git --branch "${SWIFTLINT_TAG}" --depth 1 . \
    && swift build --configuration release \
    && mv .build/release/swiftlint /usr/bin/swiftlint \
    && mv .build/release/*.so /usr/lib/swift/linux/x86_64/ \
    && mv .build/release/*.swiftmodule /usr/lib/swift/linux/x86_64/ \
    && cd / \
    && rm -rf "${SWIFTLINT_BUILD_DIR}"

RUN swiftlint version

RUN echo "${SWIFT_INSTALL_DIR}"

VOLUME ${LINT_WORK_DIR}
WORKDIR ${LINT_WORK_DIR}

ENTRYPOINT ["swiftlint"]
CMD ["lint"]
