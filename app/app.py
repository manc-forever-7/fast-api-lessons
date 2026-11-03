from fastapi import FastAPI


app =FastAPI()

@app.get("/help")


def help():
    return {"Message" : "There is no help"}