import pytest
from decimal import Decimal, getcontext

getcontext().prec = 2

class Rebalance:
    def __init__(self, current_portfolio, desired_portfolio):
        self.current_portfolio = current_portfolio
        self.desired_portfolio = desired_portfolio

    def solution(self):
        self.__validate()
        return self.__solve()

    def __validate(self):
        # just confirming that the input for current and desired is proper 
        # Sum of current_portfolio
        total_current_portfolio = 0
        for asset in self.current_portfolio:
          total_current_portfolio += self.current_portfolio[asset]

        total_desired_portfolio = 0
        for asset in self.desired_portfolio:
          total_desired_portfolio += self.desired_portfolio[asset]
        
        if total_current_portfolio != total_desired_portfolio:
          raise ValueError("Current and Desired portfolio totals do not match")
          

    def __solve(self):
      # write me
      final_allocation = {}
      over_allocation = {} # TSLA: to be sold
      under_allocation = {} # WMT: to be bought 

      current_amount = 0
      target_amount = 0

    #   current_portfolio = {"WMT": 24}
    # desired_portfolio = {"TSLA": 24}

      # Classify the assets 
      for asset in self.current_portfolio:
        current_amount = self.current_portfolio[asset]
        if asset in self.desired_portfolio:
          target_amount = self.desired_portfolio[asset]
          difference = current_amount - target_amount 
          if difference > 0: 
            over_allocation[asset] = difference 
          elif difference < 0: 
            under_allocation[asset] = -difference
        else: 
          over_allocation[asset] = current_amount
      
      # in desired but not in current then add to the under 
      for asset in self.desired_portfolio:
        if asset not in self.desired_portfolio:        
          under_allocation[asset] = self.desired_portfolio[asset]


      instructions = []

      for item in over_allocation:
        instruction = {}
        instruction["from"] = item
        instruction["to"] = {k for item in under_allocation.items()}
        instruction["amount"] = under_allocation[item]
        instructions.append(instruction)


      
        

    # current_portfolio = {"WMT": 10, "TSLA": 10}
    # desired_portfolio = {"WMT": 8, "TSLA": 8, "MSFT": 4}

      

        




      # Loop through the current and get value for current and compare desired 
      # subtract current - desired > 0 --> from: current to: desired amount 
      return []


#########
# Tests #
#########
        

def test_validates_the_current_portfolio_totals_equals_the_desired_portfolio_totals():
    current_portfolio = {"WMT": 30}
    desired_portfolio = {"TSLA": 24}

    with pytest.raises(ValueError, match="Current and Desired portfolio totals do not match"):
        Rebalance(current_portfolio, desired_portfolio).solution()


def test_it_generates_trade_instructions_for_simple_cases():
    current_portfolio = {"WMT": 24}
    desired_portfolio = {"TSLA": 24}

    trade_instructions = Rebalance(current_portfolio, desired_portfolio).solution()
    expected = [{"from": "WMT", "to": "TSLA", "amount": 24}]
    assert trade_instructions == expected


def test_it_generates_trade_instructions_for_more_complex_cases():
    current_portfolio = {"WMT": 10, "TSLA": 20}
    desired_portfolio = {"WMT": 20, "TSLA": 10}

    trade_instructions = Rebalance(current_portfolio, desired_portfolio).solution()
    trade_instructions = sort_trade_instructions(trade_instructions)

    expected = sort_trade_instructions([{"from": "TSLA", "to": "WMT", "amount": 10}])

    assert trade_instructions == expected


def test_it_creates_trade_instructions_for_new_ids():
    current_portfolio = {"WMT": 10, "TSLA": 10}
    desired_portfolio = {"WMT": 8, "TSLA": 8, "MSFT": 4}

    trade_instructions = Rebalance(current_portfolio, desired_portfolio).solution()
    trade_instructions = sort_trade_instructions(trade_instructions)

    expected = sort_trade_instructions([
        {"from": "WMT", "to": "MSFT", "amount": 2},
        {"from": "TSLA", "to": "MSFT", "amount": 2}
    ])

    assert expected == trade_instructions


def test_it_handles_precision():
    current_portfolio = {"WMT": 3.2, "TSLA": 2.1}
    desired_portfolio = {"WMT": 5, "TSLA": 0.3}

    trade_instructions = Rebalance(current_portfolio, desired_portfolio).solution()
    trade_instructions = sort_trade_instructions(trade_instructions)

    expected = sort_trade_instructions([
        {"from": "TSLA", "to": "WMT", "amount": Decimal("1.8")}
    ])

    assert expected == trade_instructions


def test_it_handles_a_bunch_of_elements():
    current_portfolio = {"WMT": 3.2, "TSLA": 2.1, "MSFT": 3.9, "AAPL": 2.8}
    desired_portfolio = {"WMT": 5.0, "TSLA": 2.4, "MSFT": 2.7, "AAPL": 1.9}

    trade_instructions = Rebalance(current_portfolio, desired_portfolio).solution()
    trade_instructions = sort_trade_instructions(trade_instructions)

    expected = sort_trade_instructions([
        {"from": "MSFT", "to": "WMT", "amount": Decimal("1.20")},
        {"from": "AAPL", "to": "TSLA", "amount": Decimal("0.30")},
        {"from": "AAPL", "to": "WMT", "amount": Decimal("0.60")},
    ])

    assert expected == trade_instructions


def test_it_works_multiple_times():
    current_portfolio = {"WMT": 3.2, "TSLA": 2.1, "MSFT": 3.9, "AAPL": 2.8}
    desired_portfolio = {"WMT": 5.0, "TSLA": 2.4, "MSFT": 2.7, "AAPL": 1.9}

    trade_instructions = Rebalance(current_portfolio, desired_portfolio).solution()
    trade_instructions = sort_trade_instructions(trade_instructions)

    expected = sort_trade_instructions([
        {"from": "MSFT", "to": "WMT", "amount": Decimal("1.20")},
        {"from": "AAPL", "to": "TSLA", "amount": Decimal("0.30")},
        {"from": "AAPL", "to": "WMT", "amount": Decimal("0.60")},
    ])

    assert expected == trade_instructions

    rebalancer = Rebalance(current_portfolio, desired_portfolio)
    trade_instructions = sort_trade_instructions(rebalancer.solution())
    assert expected == trade_instructions

    # works out when called a second time on the same instance too
    trade_instructions = sort_trade_instructions(rebalancer.solution())
    assert expected == trade_instructions

def test_it_uses_the_optimal_number_of_trades():
    current_portfolio = { "TSLA": 9, "MSFT": 3 }
    desired_portfolio = { "WMT": 4, "TSLA": 4, "MSFT": 1, "AAPL": 2, "NVDA": 1 }

    rebalancer = Rebalance(current_portfolio, desired_portfolio)
    trade_instructions = sort_trade_instructions(rebalancer.solution())

    expected = sort_trade_instructions([
      {"from": "TSLA", "to": "WMT", "amount": Decimal(4) },
      {"from": "TSLA", "to": "NVDA", "amount": Decimal(1) },
      {"from": "MSFT", "to": "AAPL", "amount": Decimal(2) },
    ])

    assert expected == trade_instructions


#######################
# Helper test methods #
#######################


def sort_trade_instructions(trade_instructions):
    return sorted(trade_instructions, key=lambda x: x["from"] + "-" + x["to"])