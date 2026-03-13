# nova-trading-agent-starter
Example trading agent that uses Sharpe Nova OS decision context before taking market risk.

# Nova Trading Agent Starter

A minimal trading agent example that queries **Sharpe Nova OS** before taking market risk.

This project demonstrates how autonomous trading systems can use Nova decision context to:

- detect elevated fragility
- adjust risk
- pause under stress
- preserve execution independence

Nova does not execute the trade.  
Nova provides context before the trade.

---

# What This Repo Shows

This starter shows a simple agent loop:

1. Observe a trade opportunity
2. Query Nova decision context
3. Evaluate regime and guardrail
4. Decide whether to:
   - proceed
   - reduce risk
   - pause

This is a decision-support example only.

---

# Core Primitive

```python
ctx = nova.context()
