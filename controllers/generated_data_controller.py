from datetime import datetime
from fastapi import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.generated_data import generated_data
from config.db import async_session
from config.logging_config import logging
from schemas.generated_data import GeneratedDataCreate

router = APIRouter()

# Dependency to get an async session
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

logger = logging.getLogger(__name__)

# API to fetch data from generated_data asynchronously
@router.get('/generated_data/fetch')
async def get_generated_data(session: AsyncSession = Depends(get_session)):
    logger.info("Processing request for /api/generated_data")
    result = await session.execute(select(generated_data))
    data = result.fetchall()
    column_names = result.keys()
    data_list = [dict(zip(column_names, row)) for row in data]
    return {
        "success": True,
        "data": data_list
    }

# API to add data to generated_data
@router.post('/generated_data/insert')
async def add_generated_data(
    data: GeneratedDataCreate,
    session: AsyncSession = Depends(get_session)
):
    logger.info("Processing request to add data to /api/generated_data")
    try:
        current_time = datetime.utcnow()  # Get current UTC time

        ins = generated_data.insert().values(
            code_mix_input=data.code_mix_input,
            pure_sinhala_output=data.pure_sinhala_output,
            is_valid=data.is_valid,
            comment=data.comment,
            updated_at=current_time,
            updated_by=data.updated_by
        )
        await session.execute(ins)
        await session.commit()

        return {
            "success": True,
            "message": "Data added successfully"
        }
    except Exception as e:
        logger.error(f"Error adding data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
