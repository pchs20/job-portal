"""User with hashed password

Revision ID: 67c030842902
Revises: 26c5b0c5c757
Create Date: 2025-03-31 19:35:16.459235

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67c030842902'
down_revision: Union[str, None] = '26c5b0c5c757'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=True))
    op.drop_column('users', 'password')


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        'users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.drop_column('users', 'hashed_password')
