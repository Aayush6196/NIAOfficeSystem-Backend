from fastapi import APIRouter

router = APIRouter()

@router.get("/cases")
def get_cases():
    return [{"id": 1, "title": "Case A"}, {"id": 2, "title": "Case B"}]
