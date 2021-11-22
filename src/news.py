import requests
from transformers import pipeline
from bs4 import BeautifulSoup

class Nnews:
    def newspull(self,coin, counter): 
        summ =  pipeline("summarization")
        ret = []
        url = "https://coinmarketcap.com/ru/currencies/"+coin+"/news/"
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        title = soup.find("meta", property="og:image")
        st = title['content']
        coinid = st.rpartition('/')[2].rpartition('.')[0]
        ll = requests.get('https://api.coinmarketcap.com/content/v3/news?coins='+coinid+'&page=1&size=10')
        data = ll.json()
        ret.append(data.get('data')[counter].get('meta').get('title')+": ")
        newsurl = data.get('data')[counter].get('meta').get('sourceUrl')
        newspage = requests.get(newsurl)
        soup2 = BeautifulSoup(newspage.text, 'html.parser')
        
        try:
            news = soup2.findAll(['h1','p'], limit=None)
            text = [result.text for result in news]
            art = ' '.join(text)
            max_chunk = 500
            art = art.replace('.', '.<eos>')
            art = art.replace('?', '?<eos>')
            art = art.replace('!', '!<eos>')
            sentences = art.split('<eos>')
            current_chunk = 0 
            chunks = []
            for sentence in sentences:
                if len(chunks) == current_chunk + 1: 
                    if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                        chunks[current_chunk].extend(sentence.split(' '))
                    else:
                        current_chunk += 1
                        chunks.append(sentence.split(' '))
                else:
                    chunks.append(sentence.split(' '))

            for chunk_id in range(len(chunks)):
                chunks[chunk_id] = ' '.join(chunks[chunk_id])
            res = summ(chunks, max_length=200, min_length=100, do_sample=False)
            rets = res[0].get('summary_text')
            print(type(rets))
            print(rets)
            ret.append(rets)
            print(ret)
            return ret
        except: AttributeError