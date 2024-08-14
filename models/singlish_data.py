from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, String

meta = MetaData()

singlish_data = Table(
    'singlish_data', meta,
    Column('singlish_sentence', String),
    Column('sinhala_sentence', String),
    Column('correctness', String)
)
