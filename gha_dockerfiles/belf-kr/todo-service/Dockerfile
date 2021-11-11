# Step 1
FROM node:14.16.1 AS builder

WORKDIR /app

## 프로젝트의 모든 파일을 WORKDIR(/app)로 복사한다
COPY . .

RUN npm i
RUN npm run build


# Step 2: 가벼운 node alpine image 사용
FROM node:14.16.1-alpine

WORKDIR /app

## Step 1의 builder에서 build된 프로젝트를 가져온다
COPY --from=builder /app ./

CMD ["npm", "run", "start:prod"]