"""initial migration

Revision ID: a5ff51ef1ea8
Revises: 
Create Date: 2024-04-08 10:55:50.603888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5ff51ef1ea8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('ingredients', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=49), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('restaurantpizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('pizza_id', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurantpizzas')
    op.drop_table('restaurants')
    op.drop_table('pizzas')
    # ### end Alembic commands ###
