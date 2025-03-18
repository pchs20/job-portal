"""Users table

Revision ID: 5ae8c1871a54
Revises: 62a5bbd475c2
Create Date: 2025-03-18 17:56:16.837070

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ae8c1871a54'
down_revision: Union[str, None] = '62a5bbd475c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('role', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
