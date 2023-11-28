"""empty message

Revision ID: efafd6cea02d
Revises: 18df6e95a610
Create Date: 2023-11-22 12:43:25.053766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'efafd6cea02d'
down_revision: Union[str, None] = '18df6e95a610'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.add_column('todo', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('todo', sa.Column('modify_date', sa.DateTime(), nullable=True))
    op.create_foreign_key(op.f('fk_todo_user_id_user'), 'todo', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_todo_user_id_user'), 'todo', type_='foreignkey')
    op.drop_column('todo', 'modify_date')
    op.drop_column('todo', 'user_id')
    op.drop_table('user')
    # ### end Alembic commands ###