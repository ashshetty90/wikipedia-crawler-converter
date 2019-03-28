
from bs4 import BeautifulSoup
import urllib2,re,yaml

class Crawler:

    CONFIG_FILE_PATH = 'config.yml'
    SEARCH_ATTRIBUTES = {
        "revenue": "Revenue",
        "operating_income": "Operating income",
        "net_income": "Net income",
        "total_assets": "Total assets",
        "total_equity": "Total equity"
    }
    def crawl(self):
        crawler_results = []
        with open(self.CONFIG_FILE_PATH, 'r') as stream:
            try:
                # loading constant values from yaml files
                config_yaml = yaml.full_load(stream)
                # setting up initial variables before making a url request
                hdr = {'User-Agent': config_yaml['user_agent']}
                request = urllib2.Request(config_yaml['wikipedia_url'], headers=hdr)
                page = urllib2.urlopen(request)
                parsed_dom = BeautifulSoup(page.read(), features=config_yaml['parser'])
                table = parsed_dom.find('table', class_=config_yaml['class'])
                # iterating through each 'tr' attribute in the vcard
                for tr in table.find_all('tr'):
                    if tr.find('th'):
                        for key, value in self.SEARCH_ATTRIBUTES.iteritems():
                            # comparing values that need to processed with the response received in each 'th'
                            if value == tr.find('th').text:
                                values_to_return = {}
                                response_values = tr.find('td').text
                                match = re.findall(r"\d+.\d+", response_values)
                                # using Converter class to convert currency values
                                values_to_return['attribute_usd_price'] = match[0]
                                values_to_return['attribute_string'] = response_values
                                values_to_return['attribute'] = value
                                # returning a list of crawler results
                                crawler_results.append(values_to_return)

                return crawler_results
            except yaml.YAMLError as exc:
                print(exc)
            except Exception as e:
                print(e)
