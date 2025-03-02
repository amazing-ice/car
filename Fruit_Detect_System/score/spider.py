import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = input('请输入需要下载图片的网址：')
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
html = requests.get(url, headers=header)
soup = BeautifulSoup(html.text, 'lxml')
img_list = soup.findAll('img')

if not os.path.isdir('./image'):
    os.mkdir('./image')

# 添加计数器
count = 0

def get_highest_resolution_url(img):
    """
    从 img 标签中获取最高分辨率的图片链接
    """
    # 检查 srcset 属性
    if 'srcset' in img.attrs:
        srcset = img['srcset']
        # srcset 格式：url1 1x, url2 2x, url3 3x
        urls = [s.strip().split(' ')[0] for s in srcset.split(',')]
        # 返回最后一个（通常是最高分辨率的）
        return urls[-1]
    
    # 检查 data-src 属性（常见于懒加载图片）
    if 'data-src' in img.attrs:
        return img['data-src']
    
    # 检查 data-srcset 属性
    if 'data-srcset' in img.attrs:
        srcset = img['data-srcset']
        urls = [s.strip().split(' ')[0] for s in srcset.split(',')]
        return urls[-1]
    
    # 默认返回 src 属性
    return img['src']

for img in img_list:
    try:
        # 只下载前300张图片
        if count >= 300:
            break

        # 获取最高分辨率的图片链接
        img_url = urljoin(url, get_highest_resolution_url(img))
        
        # 处理 alt 属性为空的情况
        alt_text = img.get('alt', 'unnamed')
        
        # 处理文件名中的非法字符
        safe_alt_text = "".join([c for c in alt_text if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()
        
        # 生成图片文件名
        image_name = f'./image/{safe_alt_text}_{count + 1}.jpg'  # 添加序号避免重名
        
        # 下载图片
        r = requests.get(img_url, stream=True)
        if r.status_code == 200:
            with open(image_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            print(f'图片 {image_name} 下载成功')
        else:
            print(f'图片 {img_url} 下载失败，状态码：{r.status_code}')
        
        # 计数器加1
        count += 1

    except Exception as e:
        print(f'图片 {img_url} 下载失败，错误信息：{e}')