"""Initial migration.

Revision ID: 8b360112ed5a
Revises: 
Create Date: 2023-02-20 21:57:54.556474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b360112ed5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cuisine', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['recipe_cuisine'])

    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cuisine_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('recipe_category_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'category', ['category_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'cuisine', ['cuisine_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
        batch_op.drop_column('recipe_cuisine')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recipe_cuisine', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('recipe_category_id_fkey', 'category', ['category_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('cuisine_id')

    with op.batch_alter_table('cuisine', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
