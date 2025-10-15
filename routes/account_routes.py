from fastapi import APIRouter, HTTPException
from account import *

router = APIRouter(prefix="/accounts", tags=["Accounts"])

