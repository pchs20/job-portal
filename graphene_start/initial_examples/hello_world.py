from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(name=String(default_value='world'))

    @staticmethod
    def resolve_hello(root, info, name):
        return f'Hello {name}'


schema = Schema(query=Query)

gql = """
{
    hello(name: "GraphQL")
}
"""


if __name__ == '__main__':
    result = schema.execute(gql)
    print(result)
