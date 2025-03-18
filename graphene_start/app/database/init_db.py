import asyncio

from app.database import async_session
from app.models import Employer, Job, User

employers_data = [
    {
        'name': 'MetaTechA',
        'contact_email': 'contact@company-a.com',
        'industry': 'Tech',
    },
    {
        'name': 'MoneySoftB',
        'contact_email': 'contact@company-b.com',
        'industry': 'Finance',
    },
]

jobs_data = [
    {
        'title': 'Software Engineer',
        'description': 'Develop web applications',
        'employer_id': 1,
    },
    {
        'title': 'Data Analyst',
        'description': 'Analyze data and create reports',
        'employer_id': 1,
    },
    {
        'title': 'Accountant',
        'description': 'Manage financial records',
        'employer_id': 2,
    },
    {
        'title': 'Manager',
        'description': 'Manage people who manage records',
        'employer_id': 2,
    },
]

users_data = [
    {
        'username': 'pduran',
        'email': 'pauduranmanzano@gmail.com',
        'password': 'securepassword',
        'role': 'admin',
    },
    {
        'username': 'useruser',
        'email': 'user@gmail.com',
        'password': 'userpassword',
        'role': 'admin',
    },
    {
        'username': 'useruser2',
        'email': 'user2@gmail.com',
        'password': 'userpassword2',
        'role': 'admin',
    },
]


async def main() -> None:
    async with async_session() as session:
        for employer in employers_data:
            employer = Employer(**employer)
            session.add(employer)
        print('Initial employers data done')
        for job in jobs_data:
            job = Job(**job)
            session.add(job)
        print('Initial jobs data done')
        for user in users_data:
            user = User(**user)
            session.add(user)
        print('Initial user data done')
        await session.commit()
        await session.close()


if __name__ == '__main__':
    asyncio.run(main())
