"""empty message

Revision ID: b39ff9fafd11
Revises: 55deaad9cd42
Create Date: 2023-04-18 18:58:51.933606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b39ff9fafd11'
down_revision = '55deaad9cd42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    with op.batch_alter_table('actor', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_actor_birthday'), ['birthday'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('actor', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_actor_birthday'))

    op.drop_table('actor')
    # ### end Alembic commands ###