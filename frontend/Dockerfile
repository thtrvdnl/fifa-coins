FROM node:12.2.0 as build

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

RUN npm install --silent
RUN npm install -g @vue/cli

COPY . /app

RUN npm run build