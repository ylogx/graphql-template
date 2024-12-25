from typing import Union

from fastapi import FastAPI

from graphql_trial import performer

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


# Define custom types for structured responses
@strawberry.type
class HelloResponse:
    message: str
    noise: float
    status: str


@strawberry.type
class ItemResponse:
    name: str
    description: str


# Define the GraphQL schema using Strawberry
@strawberry.type
class Query:
    @strawberry.field
    def hello_basic(self) -> str:
        return "Hello, GraphQL!"

    @strawberry.field
    def hello(self) -> HelloResponse:
        # noise = performer.value_generator(add_noise=True)
        message, noise = performer.perform_something()
        return HelloResponse(message=message, noise=noise, status="success")

    @strawberry.field
    def ping(self) -> str:
        return "pong"

    @strawberry.field
    def add(self, a: int, b: int) -> int:
        return a + b

    @strawberry.field
    def item(self, name: str, q: Union[str, None] = None) -> ItemResponse:
        return ItemResponse(name=name, description=f"This is the item named {name}, {q}")

    # @strawberry.field
    # def item(item_id: int, q: Union[str, None] = None):
        # return {"item_id": item_id, "q": q}

    # @app.put("/items/{item_id}")
    # def update_item(item_id: int, item: Item):
        # return {"item_name": item.name, "item_id": item_id}



app = FastAPI()

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
