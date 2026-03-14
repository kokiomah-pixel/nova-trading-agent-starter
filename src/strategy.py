def decide_from_context(ctx: dict) -> str:
    regime = ctx.get("regime")
    severity = ctx.get("guardrail", {}).get("severity")

    if regime == "Stress":
        return "pause"

    if regime == "Elevated Fragility":
        return "reduce_risk"

    if severity == "high":
        return "reduce_risk"

    return "proceed"
