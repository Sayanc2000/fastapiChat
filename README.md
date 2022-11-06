# Example Chatroom with fastapi and uvicorn

### How to run with uvicorn

`uvicorn main:app --reload`

### How to run with docker

`docker build -t chattest .`
`docker run -p 8000:8000 -it chattest`
