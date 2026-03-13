from src.nova_client import get_context
from src.strategy import decide_from_context

def main():
    ctx = get_context(asset="ETH", intent="trade", size=10000)
    action = decide_from_context(ctx)

    print("Regime:", ctx.get("regime"))
    print("Guardrail:", ctx.get("guardrail", {}).get("advisory"))
    print("Recommended action:", action)

if __name__ == "__main__":
    main()
