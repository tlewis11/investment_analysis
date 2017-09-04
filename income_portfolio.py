import logging
import json
import urllib.request
from bs4 import BeautifulSoup

#TODO: read this from a config file
my_positions = [('wmt', 4),
             ('ko', 25),
             ('cvx', 27),
             ('ge', 25),
             ('intc', 5),
             ('t', 31),
             ('xom', 30),
             ('ibm', 23),
             ('pfe', 2),
	         ('vlo', 9)]


def test_analyze_return_value():
    portfolio = Portfolio(positions=[('xom', 1)])
        
    assert 'yearly_income' in analyze(portfolio.positions).keys()


#def analyze(por
class Portfolio(object):
    def __init__(self, positions=[]):
        self.positions = positions 

    def summary(self):
        print(self.positions)
        print(analyze(self.positions))
def get_dividend_amount(symbol):
    '''
    Return dividend amount for given symbol.
    Goes to nasdaq dividned history page, looks up given stock symbol.
    '''
    stock_url = 'http://www.nasdaq.com/symbol/%s/dividend-history' %symbol
    remote_fp = urllib.request.urlopen(stock_url)

    soup = BeautifulSoup(remote_fp.read(), 'html.parser')

    amount = soup.find('table', id='quotes_content_left_dividendhistoryGrid').find('tbody').find('tr').find_all('td')[2].find('span').renderContents()
    
    #print '%s: %s' %(symbol, amount)
    remote_fp.close()
    
    return amount

def analyze(portfolio):
    total = 0
    for component in portfolio:
        print(component) 
        total = total + (float(get_dividend_amount(component[0])) * component[1] * 4)
        
    return {'yearly_income': total}


def main():
    portfolio = Portfolio(positions=my_positions)     
    portfolio.summary()
if __name__ == '__main__':
    #test_analyze_return_value()
    main()
