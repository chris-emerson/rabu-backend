"""Example fixtures for the Google Search Custom Endpoint AI"""
MOCK_IMAGE_URL = "http://mock.jpg"

GOOGLE_SEARCH_RESPONSE = {
                "items": [
                    {
                        "pagemap": {
                            "cse_image": [{
                                "src": MOCK_IMAGE_URL
                            }]
                        }
                    }
                ]
            }
