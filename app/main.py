from fastapi import FastAPI
import socket
import os

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "v1")

@app.get("/")
def root():
        return {
                "message":"FASTAPI DEVOPS APP",
                "version": APP_VERSION
}

@app.get("/health")
def health():
        return{"status": "ok"}

@app.get("/version")
def version():
        return{"version": APP_VERSION}

@app.get("/hostname")
def hostname():
        return{"hostname": socket.gethostname()}