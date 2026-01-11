import os

def get_service_info():
	return {
		"service": os.getenv("SERVICE_NAME", "reusable-backend"),
		"version": os.getenv("SERVICE_VERSION", "1.0.0"),
		"environment": os.getenv("ENVIRONMENT", "local")
	}
