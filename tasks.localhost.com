server {
  listen 80;

  server_name tasks.localhost.com;
  proxy_buffering off;

  proxy_set_header Host $http_host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-Proto $scheme;

  location / {
    proxy_pass http://127.0.0.1:3000/;
  }

  location /api {
    proxy_pass http://127.0.0.1:3001;
  }
}