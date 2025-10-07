# DOCKER + fast — Simple FastAPI app

Minimal FastAPI app packaged with Docker.

Prerequisites
- Docker installed

Build the Docker image
```sh
docker build -t simple_fastapiapp:v1 .
```

Run the container (default maps host 3002 → container 3002)
```sh
docker run -p 3002:3002 simple_fastapiapp:v1
```

Access
- Website: http://localhost:3002/
- Swagger UI: http://localhost:3002/docs)

Virtual environment (exact commands provided):

```
# create environment
uv venv

# activate
.venv\Scripts\activate

# install required library versions
uv pip install -r requirements.txt

# deactivate
deactivate
```
