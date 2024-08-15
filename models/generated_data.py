from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

meta = MetaData()

generated_data = Table(
    'generated_data', meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('code_mix_input', String, nullable=False),
    Column('pure_sinhala_output', String),
    Column('is_valid', String),
    Column('comment', String),
    Column('updated_at', DateTime),
    Column('updated_by', String)
)
