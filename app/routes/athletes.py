from fastapi import APIRouter, HTTPException
from app.services.athletes import get_athlete_data, compute_athlete_stats

router = APIRouter(prefix="/athletes", tags=["Athlètes"])

FFCK_BASE_URL = "https://cna-slalom.nicolas-abbal.com/api/ffck/boats/C1H282170"

@router.get("/", summary="Statistiques d’un athlète")
def get_athlete_stats():
    data = get_athlete_data()
    stats = compute_athlete_stats(data)
    return stats


