from pydantic import BaseModel

class Strategy(BaseModel):
    name: str
    parameters: dict

class BacktestResult(BaseModel):
    strategy_name: str
    profit_loss: float
    other_metrics: dict  # Placeholder for other metrics like drawdown, trades made, etc.