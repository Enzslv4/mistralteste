import wandb

def log_performance_metrics(student_id: str, topic: str, score: float, time_spent: int):
    wandb.init(project="educacao-personalizada", anonymous="allow")
    wandb.log({
        "student_id": student_id,
        "topic": topic,
        "score": score,
        "time_spent": time_spent
    })
    wandb.finish()
