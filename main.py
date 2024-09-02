from fastapi import FastAPI

app = FastAPI(title="review-and-rating-svc", description="Review and Rating Service", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
