import asyncio

from app.database import async_session
from app.models import Employer, Job

employers_data = [
    {
        'id': 1,
        'name': 'MetaTechA',
        'contact_email': 'contact@company-a.com',
        'industry': 'Tech',
    },
    {
        'id': 2,
        'name': 'MoneySoftB',
        'contact_email': 'contact@company-b.com',
        'industry': 'Finance',
    },
]

jobs_data = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'description': 'Develop web applications',
        'employer_id': 1,
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'description': 'Analyze data and create reports',
        'employer_id': 1,
    },
    {
        'id': 3,
        'title': 'Accountant',
        'description': 'Manage financial records',
        'employer_id': 2,
    },
    {
        'id': 4,
        'title': 'Manager',
        'description': 'Manage people who manage records',
        'employer_id': 2,
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
        await session.commit()
        await session.close()


if __name__ == '__main__':
    asyncio.run(main())
