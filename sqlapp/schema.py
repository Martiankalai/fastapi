from pydantic import BaseModel


class SubPageBase(BaseModel):
    heading: str
    description: str
    footer: str
    pg_no: int
    pg_dim: float


class SubPageCreate(SubPageBase):
    pass


class SubPage(SubPageBase):
    id: int

    class Config:
        orm_mode = True
