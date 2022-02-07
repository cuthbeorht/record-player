"""create todos table

Revision ID: 07ff35e3796d
Revises: 
Create Date: 2022-02-02 20:52:29.079353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07ff35e3796d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todos",
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.Text),
        sa.Column('description', sa.Text),
        sa.Column('created_by', sa.Text),
        sa.Column('created', sa.TIMESTAMP)
    )


def downgrade():
    op.drop_table('todos')
