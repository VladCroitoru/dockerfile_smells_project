FROM public.ecr.aws/lambda/nodejs:14

RUN npm install -g npm

COPY ./ ./

ARG NEXTAUTH_URL
ARG NEXT_PUBLIC_GA_PROPERTY_ID
ARG NEXT_PUBLIC_SOCIAL_CARE_APP_URL
ARG CSRF_SECRET

ENV NEXTAUTH_URL=${NEXTAUTH_URL}
ENV NEXT_PUBLIC_GA_PROPERTY_ID=${NEXT_PUBLIC_GA_PROPERTY_ID}
ENV NEXT_PUBLIC_SOCIAL_CARE_APP_URL=${NEXT_PUBLIC_SOCIAL_CARE_APP_URL}
ENV CSRF_SECRET=${CSRF_SECRET}

RUN rm -rf ./node_modules/ \
    && npm install \
    && npm run build:app

RUN rm -rf ./node_modules/ \
    && npm install --production \
    && npm install prisma@2.30.3 \
    && npm run build:prisma
