"""User role as enum

Revision ID: b7d5a8a50a99
Revises: 67c030842902
Create Date: 2025-04-19 18:44:19.596191

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7d5a8a50a99'
down_revision: Union[str, None] = '67c030842902'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    user_role_enum = sa.Enum('admin', 'employer', 'applicant', name='userroleenum')
    user_role_enum.create(op.get_bind())
    op.execute(
        """
        ALTER TABLE users
        ALTER
        COLUMN role
        TYPE userroleenum
        USING role::userroleenum
       """
    )


def downgrade() -> None:
    """Downgrade schema."""
    user_role_enum = sa.Enum('admin', 'employer', 'applicant', name='userroleenum')
    op.execute(
        """
        ALTER TABLE users
        ALTER
        COLUMN role
        TYPE VARCHAR
        USING role::VARCHAR
       """
    )
    user_role_enum.drop(op.get_bind())
