from graphene import Field, Int, List, Mutation, ObjectType, String, Schema


class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()


class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        age = Int(required=True)

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, name, age):
        user = {'id': len(Query.users) + 1, 'name': name, 'age': age}
        Query.users.append(user)
        return CreateUser(user=user)


class UpdateUser(Mutation):
    class Arguments:
        user_id = Int(required=True)
        name = String()
        age = Int()

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, user_id, name=None, age=None):
        matched_users = [user for user in Query.users if user['id'] == user_id]
        if not matched_users:
            return None
        user = matched_users[0]
        if name is not None:
            user['name'] = name
        if age is not None:
            user['age'] = age
        return UpdateUser(user=user)


class DeleteUser(Mutation):
    class Arguments:
        user_id = Int(required=True)

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, user_id):
        for i, u in enumerate(Query.users):
            if u['id'] == user_id:
                user = u
                del Query.users[i]
                return DeleteUser(user=user)


class Query(ObjectType):
    user = Field(UserType, user_id=Int())
    user_by_min_age = List(UserType, min_age=Int())

    # example data for testing
    users = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 35},
        {'id': 3, 'name': 'Charlie', 'age': 40},
        {'id': 4, 'name': 'David', 'age': 45},
    ]

    @staticmethod
    def resolve_user(root, info, user_id: int):
        matched_users = [user for user in Query.users if user['id'] == user_id]
        # ToDo (pduran): Raise an http 404 exception if no user is found
        return matched_users[0] if matched_users else None

    @staticmethod
    def resolve_user_by_min_age(root, info, min_age):
        return [user for user in Query.users if user['age'] >= min_age]


class Mutation(ObjectType):  # type: ignore
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


schema = Schema(query=Query, mutation=Mutation)

gql_query_user = """
query {
    user(userId: 5) {
        id
        name
        age
    }
}
"""

gql_query_user_by_min_age = """
query {
    userByMinAge(minAge: 40) {
        id
        name
        age
    }
}
"""

gql_create_user = """
mutation {
    createUser(name: "Eve", age: 50) {
        user {
            id
            name
            age
        }
    }
}
"""

gql_update_user = """
mutation {
    updateUser(userId: 5, name: "Evelyn") {
        user {
            id
            name
            age
        }
    }
}
"""

gql_delete_user = """
mutation {
    deleteUser(userId: 5) {
        user {
            id
            name
            age
        }
    }
}
"""


if __name__ == '__main__':
    result = schema.execute(gql_query_user)
    print(result)
    result = schema.execute(gql_create_user)
    print(result)
    result = schema.execute(gql_query_user)
    print(result)
    result = schema.execute(gql_update_user)
    print(result)
    result = schema.execute(gql_query_user)
    print(result)
    result = schema.execute(gql_delete_user)
    print(result)
    result = schema.execute(gql_query_user)
    print(result)
