import deposit_loan
import investments
import loan_to_deposit_ratio
import market_share
import mortgages
from main import app
from flask import render_template
from os import path



@app.route('/')
def index():
    bank_url = r"C:\Users\Pitso\Downloads\BA900SampleData\2021-10-01"
    deposits_and_loans = deposit_loan.run(parent_url=bank_url)

    bank_market_share = market_share.run(parent_url=bank_url)

    ldr = loan_to_deposit_ratio.run(parent_url=path.dirname(bank_url))

    mortgage = mortgages.run(parent_url=path.dirname(bank_url))

    investment = investments.run(parent_url=path.dirname(bank_url))

    return render_template('index.html', deposits_and_loans=deposits_and_loans,
                           bank_market_share=bank_market_share,
                           ldr=ldr,
                           mortgage=mortgage,
                           investment=investment)
