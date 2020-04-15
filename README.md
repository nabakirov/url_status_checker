# url status checker

## Installation
```shell script
git clone https://github.com/nabakirov/url_status_checker.git
cd url_status_checker && docker-compose up -d
```
Server will start on port 8000

## create super user
```shell script
docker exec -it backend sh
./manage.py createsuperuser
```

## API
### login
```shell script
curl --request POST \
  --url http://localhost:8000/api/v1/login/ \
  --header 'content-type: application/json' \
  --data '{
	"username": "username",
	"password": "password"
}'
```
response
```json5
{
  "refresh": "token",
  "access": "token"
}
```
### refresh access token
```shell script
curl --request POST \
  --url http://localhost:8000/api/v1/refresh/ \
  --header 'content-type: application/json' \
  --data '{
	"refresh": "token"
}'
```
response
```json5
{
  "access": "token"
}
```
### list of urls (async updates)
```shell script
curl --request GET \
  --url http://localhost:8000/api/v1/urls/ \
  --header 'authorization: Bearer AccessToken'
```
response
```json5
[
  {
    "id": "int",
    "url": "str",
    "status_code": "int"
  }
]
```