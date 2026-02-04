import wandb


def promote_if_better(
    new_metric: float,
    baseline_metric: float,
    artifact_path: str,
):
    if new_metric > baseline_metric:
        artifact = wandb.Artifact(
            name="fusion_model",
            type="model",
        )
        artifact.add_file(artifact_path)
        wandb.log_artifact(artifact)
        return True
    return False
