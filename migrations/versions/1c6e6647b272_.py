"""empty message

Revision ID: 1c6e6647b272
Revises: ed26d02301d5
Create Date: 2024-10-03 19:46:55.510278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c6e6647b272'
down_revision = 'ed26d02301d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('birth_year', sa.String(length=150), nullable=False),
    sa.Column('eye_color', sa.String(length=150), nullable=False),
    sa.Column('films', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('gender', sa.String(length=150), nullable=False),
    sa.Column('hair_color', sa.String(length=150), nullable=False),
    sa.Column('height', sa.String(length=150), nullable=False),
    sa.Column('homeworld', sa.String(length=150), nullable=False),
    sa.Column('mass', sa.String(length=150), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('skin_color', sa.String(length=150), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('edited_at', sa.DateTime(), nullable=False),
    sa.Column('species', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('starships', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('url', sa.String(length=150), nullable=False),
    sa.Column('vehicles', sa.ARRAY(sa.String()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=150), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('edited_at', sa.DateTime(), nullable=False),
    sa.Column('diameter', sa.String(length=150), nullable=False),
    sa.Column('films', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('gravity', sa.String(length=150), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('orbital_period', sa.String(length=150), nullable=False),
    sa.Column('population', sa.String(length=150), nullable=False),
    sa.Column('residents', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('rotation_period', sa.String(length=150), nullable=False),
    sa.Column('surface_water', sa.String(length=150), nullable=False),
    sa.Column('terrain', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=450), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(length=455), nullable=True))
        batch_op.add_column(sa.Column('person_id', sa.Integer(), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['url'])
        batch_op.create_foreign_key(None, 'person', ['person_id'], ['id'])
        batch_op.drop_column('description')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('name',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('person_id')
        batch_op.drop_column('url')

    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('favorites')
    op.drop_table('planets')
    op.drop_table('users')
    op.drop_table('planet')
    op.drop_table('person')
    # ### end Alembic commands ###
