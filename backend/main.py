import uvicorn

# this is a stub that serves as the entry point for the module
# defines the port, ip host, and reload settings
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
