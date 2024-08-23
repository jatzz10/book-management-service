"""Initial migration.

Revision ID: 0CD63247
Revises:
Create Date: 2024-08-18 11:46:00.000000

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

from app import db
from app.models.reviews import RatingEnum

# revision identifiers, used by Alembic.
revision = '0CD63247'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('books',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=150), nullable=False),
                    sa.Column('author', sa.String(length=100), nullable=False),
                    sa.Column('genre', sa.String(length=20)),
                    sa.Column('year_published', sa.String(length=10)),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), default=datetime.now()),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), default=datetime.now(), onupdate=datetime.now()),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('reviews',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('book_id', sa.Integer(), sa.ForeignKey('books.id')),
                    sa.Column('user_id', sa.String(length=50), nullable=False, default=''),
                    sa.Column('review_text', sa.Text(), nullable=False, default=''),
                    sa.Column('rating', sa.Enum(RatingEnum), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), default=datetime.now()),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), default=datetime.now(), onupdate=datetime.now()),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['book_id'], ['books.id'], )
                    )


def downgrade():
    op.drop_table('reviews')
    op.drop_table('books')
