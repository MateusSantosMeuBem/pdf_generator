# --------- BUILT-IN PACKAGES ---------
import json

file_path: str = r'C:\Users\Mateus\projects\python\generate_paper_page\src\data\code_for_begginers.json'

with open(
    file=file_path,
    mode='r',
    encoding='utf-8'
) as file_: 
    content: list = json.load(file_)

for data in content['data']:
    title: str = data['title']
    description: str = data['description']
    urls: list[dict[str, str]] = data['urls']
    print(f'Title: {title}')
    print(f'Description: {description}')
    
    for url in urls:
        print(f'\tTitle_url: {url["title"]}')
        print(f'\tUrl: {url["url"]}')

    print('-'*80, end='\n\n')
