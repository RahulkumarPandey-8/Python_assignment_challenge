from flask import Flask, render_template, request
from autoscraper import AutoScraper

app = Flask(__name__)

# Define the Amazon AutoScraper instance
amazon_scraper = AutoScraper()

# Define the scraper rules for Amazon search results
amazon_scraper.load('amazon-search')

def get_amazon_result(search_query):
    url = f'https://www.amazon.in/s?k={search_query}'
    # Update the scraper to ensure accurate scraping
    amazon_scraper.set_rule_aliases({'rule_1': 'Title'})
    # Scrape Amazon search results for the provided query
    result = amazon_scraper.get_result_similar(url, group_by_alias=True)
    return result

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    # Get the search query from the request parameters
    query = request.args.get('q')
    
    # Scrape Amazon search results for the provided query
    amazon_results = get_amazon_result(query)
    
    # Render the search results using the 'results.html' template
    return render_template('results.html', query=query, amazon_results=amazon_results)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
