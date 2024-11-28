from typing import Optional, TypedDict


class Config(TypedDict):
    title: Optional[str]
    description: Optional[str]
    name: Optional[str]
    email: Optional[str]
    combine_output: bool
