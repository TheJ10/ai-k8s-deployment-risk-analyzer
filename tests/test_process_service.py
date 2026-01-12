from app.services.process_service import process_input

def test_process_input():
	result = process_input("cloud")
	assert result["original"] == "cloud"
	assert result["length"] == 5
	assert result["uppercase"] == "CLOUD"
