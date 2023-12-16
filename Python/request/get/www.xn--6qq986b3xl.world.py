from tqdm import tqdm
import requests

result = []
for i in tqdm(range(100)):
    result.append(requests.get('https://www.xn--6qq986b3xl.world/'))

print(result)