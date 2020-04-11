"""empty message

Revision ID: 1e662fc655e6
Revises: 734db62451e5
Create Date: 2020-04-11 01:12:27.746861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e662fc655e6'
down_revision = '734db62451e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('profiles', 'biography',
               existing_type=sa.TEXT(),
               comment=None,
               existing_comment='This field stores personal information of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'date_joined',
               existing_type=sa.VARCHAR(length=100),
               comment=None,
               existing_comment='This field records date activity ',
               existing_nullable=True)
    op.alter_column('profiles', 'email',
               existing_type=sa.VARCHAR(length=100),
               comment=None,
               existing_comment='This field stores the email of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               comment=None,
               existing_comment='This field store the first name of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'gender',
               existing_type=sa.VARCHAR(length=20),
               comment=None,
               existing_comment='This field stores the gender of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'last_name',
               existing_type=sa.VARCHAR(length=100),
               comment=None,
               existing_comment='This field stores the last name of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'location',
               existing_type=sa.VARCHAR(length=100),
               comment=None,
               existing_comment='This field stores the location of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'profile_picture',
               existing_type=sa.VARCHAR(length=100),
               comment=None,
               existing_comment='This field stores a profile picture link',
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('profiles', 'profile_picture',
               existing_type=sa.VARCHAR(length=100),
               comment='This field stores a profile picture link',
               existing_nullable=True)
    op.alter_column('profiles', 'location',
               existing_type=sa.VARCHAR(length=100),
               comment='This field stores the location of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'last_name',
               existing_type=sa.VARCHAR(length=100),
               comment='This field stores the last name of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'gender',
               existing_type=sa.VARCHAR(length=20),
               comment='This field stores the gender of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               comment='This field store the first name of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'email',
               existing_type=sa.VARCHAR(length=100),
               comment='This field stores the email of the user',
               existing_nullable=True)
    op.alter_column('profiles', 'date_joined',
               existing_type=sa.VARCHAR(length=100),
               comment='This field records date activity ',
               existing_nullable=True)
    op.alter_column('profiles', 'biography',
               existing_type=sa.TEXT(),
               comment='This field stores personal information of the user',
               existing_nullable=True)
    # ### end Alembic commands ###