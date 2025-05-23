# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Add tables for SQL Lab state

Revision ID: db4b49eb0782
Revises: 78ee127d0d1d
Create Date: 2019-11-13 11:05:30.122167

"""

import sqlalchemy as sa
from alembic import op

from superset.migrations.shared.utils import create_table

# revision identifiers, used by Alembic.
revision = "db4b49eb0782"
down_revision = "78ee127d0d1d"


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    create_table(
        "tab_state",
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("changed_on", sa.DateTime(), nullable=True),
        sa.Column("extra_json", sa.Text(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("label", sa.String(length=256), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.Column("database_id", sa.Integer(), nullable=True),
        sa.Column("schema", sa.String(length=256), nullable=True),
        sa.Column("sql", sa.Text(), nullable=True),
        sa.Column("query_limit", sa.Integer(), nullable=True),
        sa.Column("latest_query_id", sa.String(11), nullable=True),
        sa.Column("autorun", sa.Boolean(), nullable=False, default=False),
        sa.Column("template_params", sa.Text(), nullable=True),
        sa.Column("created_by_fk", sa.Integer(), nullable=True),
        sa.Column("changed_by_fk", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["changed_by_fk"], ["ab_user.id"]),
        sa.ForeignKeyConstraint(["created_by_fk"], ["ab_user.id"]),
        sa.ForeignKeyConstraint(["database_id"], ["dbs.id"]),
        sa.ForeignKeyConstraint(["latest_query_id"], ["query.client_id"]),
        sa.ForeignKeyConstraint(["user_id"], ["ab_user.id"]),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_index(op.f("ix_tab_state_id"), "tab_state", ["id"], unique=True)
    create_table(
        "table_schema",
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("changed_on", sa.DateTime(), nullable=True),
        sa.Column("extra_json", sa.Text(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("tab_state_id", sa.Integer(), nullable=True),
        sa.Column("database_id", sa.Integer(), nullable=False),
        sa.Column("schema", sa.String(length=256), nullable=True),
        sa.Column("table", sa.String(length=256), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("expanded", sa.Boolean(), nullable=True),
        sa.Column("created_by_fk", sa.Integer(), nullable=True),
        sa.Column("changed_by_fk", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["changed_by_fk"], ["ab_user.id"]),
        sa.ForeignKeyConstraint(["created_by_fk"], ["ab_user.id"]),
        sa.ForeignKeyConstraint(["database_id"], ["dbs.id"]),
        sa.ForeignKeyConstraint(["tab_state_id"], ["tab_state.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_index(op.f("ix_table_schema_id"), "table_schema", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_table_schema_id"), table_name="table_schema")
    op.drop_table("table_schema")
    op.drop_index(op.f("ix_tab_state_id"), table_name="tab_state")
    op.drop_table("tab_state")
    # ### end Alembic commands ###
