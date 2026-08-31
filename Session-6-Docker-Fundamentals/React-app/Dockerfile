FROM node:24-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

FROM nginx:1.28-alpine
COPY index.html /usr/share/nginx/html/index.html
COPY --from=build /app/node_modules/react/umd/react.production.min.js /usr/share/nginx/html/react.production.min.js
COPY --from=build /app/node_modules/react-dom/umd/react-dom.production.min.js /usr/share/nginx/html/react-dom.production.min.js
EXPOSE 80
