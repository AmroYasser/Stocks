# Stocks

A web app -integreted with [Alpha Vantage's](https://www.alphavantage.co/) API- that allows the user to browse the list of stocks in the S&P 500 graph.


## Building

Use Docker commands as following to build the environment

```bash
docker build -t stocks .
docker run -p 9000:9000 stocks
```

## Run tests


```bash
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements
python tests
```


## Usage
- You can not access the actual data if you're not logged in. So the home page redirects the non-authenticated user to the log in page, and if you don't have an account, you should register first.

- To access the companies' list, go to
[http://127.0.0.1:9000/]()

- Then click on a company, this will redirect you to [http://127.0.0.1:9000/api/stock_price?sympol=\{\{ company.sympol \}\}]()
 to see its stocks graph. 

- Each user has a profile page only him can access.


## Notes

The [provided API](https://www.alphavantage.co/documentation/) requires registeration to get full access, so we used the demo version which provides only IBM support, that is why I hardcoded it

```bash
<h2><a href={% url 'stock_prices' %}?symbol=IBM>{{ company.name }}</a></h2>
```

If, instead, we had an account this line should be re-written to 
```bash
<h2><a href={% url 'stock_prices' %}?symbol={{company.symbol}}>{{ company.name }}</a></h2>
```
