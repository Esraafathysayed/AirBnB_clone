#!/usr/bin/env python3
from models.base_models import BaseModel


class User(BaseModel):
    """User instance"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
