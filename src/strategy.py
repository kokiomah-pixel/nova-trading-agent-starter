def decide_from_context(ctx: dict) -> str:
    regime = ctx.get("regime")
    severity = ctx.get("guardrail", {}).get("severity")

    if regime == "Stress":
        return "pause"

    if severity == "high":
        return "reduce_risk"

    return "proceed"
