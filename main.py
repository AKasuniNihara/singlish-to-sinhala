from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.middleware.cors import CORSMiddleware

from config.db import async_session
from models.index import singlish_data
from config.logging_config import logging
from controllers.generated_data_controller import router as generated_data_router


app = FastAPI()

origins = [
    "http://localhost:8080",  # Replace with your frontend origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get an async session
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

logger = logging.getLogger(__name__)

# API to fetch data asynchronously
@app.get('/api/singlish_data')
async def index(session: AsyncSession = Depends(get_session)):
    logger.info("Processing request for /api/singlish_data")
    result = await session.execute(select(singlish_data))
    data = result.fetchall()
    # print(f"Data type: {type(data)}")
    # print(f"Data content: {data}")
    # Convert each row to a dictionary
    column_names = result.keys()
    data_list = [dict(zip(column_names, row)) for row in data]
    return {
        "success": True,
        "data": data_list
    }

# Register the new router for generated_data endpoints
app.include_router(generated_data_router, prefix="/api")