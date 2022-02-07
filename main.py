import yfinance as yf
import plotly.graph_objects as go
import webbrowser

def search_Stock(tkr):
    import yfinance as yf
    stock = yf.Ticker(tkr)
    return stock

def define_Stock():
    import yfinance as yf
    stock = yf.Ticker(input(str("Enter stock ticker: ")))
    return stock

def create_Graph(stock):
    import plotly.graph_objects as go
    
    company_Name = stock.info['longName']
    
    history = stock.history(period='max')
    
    fig = go.Figure(data=go.Scatter(x=history.index, y=history['Close'],mode='lines'))
    fig.update_layout(title_text=str(company_Name), title_x=0.5)
    
    return fig


def main():
    stock = define_Stock()
    mainloop = True
    while mainloop == True:
        company_Name = stock.info['longName']
        print('Current selection: ' +str(company_Name))
        options = ['1)Stock news.', '2)Stock info.', '3)Dividend info.', '4)Stock graph.','5)Company financials.','6)Open logo (new window).','7)Change stock.', '8)End.']
        print('Select an option: ')

        for i in options:
            print(i)

        selection = input("Enter selection 1-" +str(len(options)) +str(':'))

        if selection == '1':
            news = str(stock.news)
            news_arr = news.split(', ')
            for i in news_arr:
                print(i)
            
            
        elif selection == '2':
            info = str(stock.info)
            info_arr = info.split(', ')
            for i in info_arr:
                print(i)
            
        elif selection == '3':
            print(stock.dividends)
        
        elif selection == '4':
            create_Graph(stock).show()
        
        elif selection == '5':
            print(stock.financials)
        
        elif selection == "6":
            webbrowser.open(stock.info['logo_url'])
        
        elif selection == '7':
            stock = define_Stock()
        
        elif selection == '8':
            mainloop = False
        else:
            print('Please try again.')
          
main()














