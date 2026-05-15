from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.middleware("http")(timer_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issues_router)


@app.get("/")
async def root():
    return {"message": "Hello"}

# items = [
#     {"id": 1, "name": "Item 1"},
#     {"id": 2, "name": "Item 2"},
#     {"id": 3, "name": "Item 3"},
# ]
# @app.get("/")
# def health_check():
#     return {"status": "ok"}
# @app.get("/items")
# def get_items():
#     return items
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     return {"error": "Item not found"}
# @app.post("/items")
# def create_item(item: dict):
#     new_id = max(item["id"] for item in items) + 1
#     item["id"] = new_id
#     items.append(item)
#     return item
