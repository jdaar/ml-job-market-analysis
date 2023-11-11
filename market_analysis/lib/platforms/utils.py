from proxyscrape import create_collector

def retrieve_proxy() -> str:
    collector = create_collector('http-collector', 'http')
    proxy = collector.get_proxy()
    return proxy