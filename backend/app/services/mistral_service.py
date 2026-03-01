import requests

def generate_feedback(student_id: str, topic: str, score: float):
    response = requests.post(
        "https://api.mistral.ai/v1/feedback",
        json={
            "student_id": student_id,
            "topic": topic,
            "score": score
        }
    )
    return response.json()
