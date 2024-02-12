#!/usr/bin/env python3
"""Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """User instance"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
