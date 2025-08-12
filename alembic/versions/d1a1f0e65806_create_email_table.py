"""create email table

Revision ID: d1a1f0e65806
Revises: 
Create Date: 2025-08-07 15:27:45.457167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1a1f0e65806'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'email',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('recipient', sa.String(255), nullable=False),
        sa.Column('subject', sa.String(255)),
        sa.Column('body', sa.Text),
        sa.Column('status', sa.String(50)),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

def downgrade():
    op.drop_table('email')
