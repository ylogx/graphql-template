from typing import Union

from fastapi import FastAPI
#from pydantic import BaseModel

from graphql_trial import performer

# Python GraphQL server using Strawberry
# Install dependencies: pip install strawberry-graphql fastapi uvicorn

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# Define the GraphQL schema using Strawberry
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, GraphQL!"

    @strawberry.field
    def ping(self) -> str:
        return "pong"

    @strawberry.field
    def add(self, a: int, b: int) -> int:
        return a + b

    # @strawberry.field
    # def item(item_id: int, q: Union[str, None] = None):
        # return {"item_id": item_id, "q": q}


schema = strawberry.Schema(Query)

# Set up FastAPI with the GraphQL route
app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Run the server
# Use `uvicorn graphql_python_server:app --reload` to run this server


#@app.put("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, "item_id": item_id}