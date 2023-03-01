# thirdparty
from fastapi import FastAPI, Query

# project
from web.controllers import index

app = FastAPI()
index.register_routes(app)


if __name__ == '__main__':
    # thirdparty
    import uvicorn

    uvicorn.run("main:app")
