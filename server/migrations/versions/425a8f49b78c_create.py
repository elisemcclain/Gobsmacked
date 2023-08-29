"""Create

Revision ID: 425a8f49b78c
Revises: 
Create Date: 2023-08-28 16:21:16.492144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425a8f49b78c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('goblins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('traits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('grubnub_win', sa.Integer(), nullable=False),
    sa.Column('sneezle_win', sa.Integer(), nullable=False),
    sa.Column('blort_win', sa.Integer(), nullable=False),
    sa.Column('grimble_win', sa.Integer(), nullable=False),
    sa.Column('zongos_win', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('dialogues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_part', sa.Integer(), nullable=False),
    sa.Column('date_id', sa.Integer(), nullable=False),
    sa.Column('trait_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['date_id'], ['dates.id'], name=op.f('fk_dialogues_date_id_dates')),
    sa.ForeignKeyConstraint(['trait_id'], ['traits.id'], name=op.f('fk_dialogues_trait_id_traits')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outcomes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_id', sa.Integer(), nullable=False),
    sa.Column('goblin_id', sa.Integer(), nullable=False),
    sa.Column('outcome_description', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['date_id'], ['dates.id'], name=op.f('fk_outcomes_date_id_dates')),
    sa.ForeignKeyConstraint(['goblin_id'], ['goblins.id'], name=op.f('fk_outcomes_goblin_id_goblins')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trait_associations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('trait_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trait_id'], ['traits.id'], name=op.f('fk_trait_associations_trait_id_traits')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_trait_associations_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('responses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dialogue_id', sa.Integer(), nullable=False),
    sa.Column('goblin_id', sa.Integer(), nullable=False),
    sa.Column('response', sa.String(), nullable=False),
    sa.Column('outcome', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['dialogue_id'], ['dialogues.id'], name=op.f('fk_responses_dialogue_id_dialogues')),
    sa.ForeignKeyConstraint(['goblin_id'], ['goblins.id'], name=op.f('fk_responses_goblin_id_goblins')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('responses')
    op.drop_table('trait_associations')
    op.drop_table('outcomes')
    op.drop_table('dialogues')
    op.drop_table('users')
    op.drop_table('traits')
    op.drop_table('goblins')
    op.drop_table('dates')
    # ### end Alembic commands ###
