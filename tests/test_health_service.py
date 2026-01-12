from app.services.health_service import get_health_status

def test_health_status():
	result = get_health_status()
	assert result["status"] == "ok"
