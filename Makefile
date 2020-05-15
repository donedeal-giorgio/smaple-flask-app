build:
	docker build . --tag moviesite:latest

run:
	docker run -it --rm -p 8080:8080 --env-file .env moviesite:latest
