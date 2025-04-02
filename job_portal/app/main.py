from fastapi import FastAPI

from graphene import Schema

from starlette_graphene3 import (
    GraphQLApp,
    make_graphiql_handler,
    make_playground_handler,
)

from app.gql import Mutation, Query

schema = Schema(query=Query, mutation=Mutation)

app = FastAPI()

app.mount(
    '/graphql',
    GraphQLApp(schema=schema, on_get=make_graphiql_handler()),
)

app.mount(
    '/graphql-p',
    GraphQLApp(schema=schema, on_get=make_playground_handler()),
)
