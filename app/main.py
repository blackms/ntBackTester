# Import FastAPI and other necessary modules
from fastapi import FastAPI
from models import Strategy, BacktestResult
# Initialize the FastAPI app
app = FastAPI()

# In-memory database
strategies_db = []
results_db = []

# Define a simple root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Crypto Backtester Service!"}

@app.post("/strategy/")
def add_strategy(strategy: Strategy):
    strategies_db.append(strategy)
    return {"message": "Strategy added successfully!"}

@app.post("/backtest/")
def initiate_backtest(strategy_name: str):
    # Mock backtesting logic
    result = BacktestResult(strategy_name=strategy_name, profit_loss=100.0, other_metrics={})
    results_db.append(result)
    return {"message": "Backtest completed!", "result": result}

@app.get("/results/")
def get_results():
    return results_db

# This block allows you to run the app directly using Uvicorn if needed
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
