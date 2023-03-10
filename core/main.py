# thirdparty
from fastapi import FastAPI

# project
from controllers import index

app = FastAPI()
index.register_routes(app)


if __name__ == "__main__":
    # thirdparty
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=80)
