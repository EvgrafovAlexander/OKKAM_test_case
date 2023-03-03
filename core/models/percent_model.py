# thirdparty
from pydantic import BaseModel, Field


class PercentModel(BaseModel):
    """Модель процента вхождения второй аудитории в первую"""

    percent: float = Field(title="Процент вхождения второй аудитории в первую")
