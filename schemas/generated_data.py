from pydantic import BaseModel
from typing import Optional

class GeneratedDataCreate(BaseModel):
    code_mix_input: str
    pure_sinhala_output: Optional[str] = None
    is_valid: Optional[str] = None
    comment: Optional[str] = None
    updated_by: Optional[str] = None
