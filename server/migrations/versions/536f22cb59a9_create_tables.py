"""Create tables

Revision ID: 536f22cb59a9
Revises: 425a8f49b78c
Create Date: 2023-08-30 09:47:00.620194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536f22cb59a9'
down_revision = '425a8f49b78c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dates', schema=None) as batch_op:
        batch_op.add_column(sa.Column('part_1', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('part_2', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('part_3', sa.String(), nullable=False))

    with op.batch_alter_table('goblins', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_url', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('artist', sa.String(), nullable=False))

    with op.batch_alter_table('outcomes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('result', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('outcomes', schema=None) as batch_op:
        batch_op.drop_column('result')

    with op.batch_alter_table('goblins', schema=None) as batch_op:
        batch_op.drop_column('artist')
        batch_op.drop_column('img_url')

    with op.batch_alter_table('dates', schema=None) as batch_op:
        batch_op.drop_column('part_3')
        batch_op.drop_column('part_2')
        batch_op.drop_column('part_1')

    # ### end Alembic commands ###
