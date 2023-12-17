import requests
import time
import os
import tqdm
import threading

class main:
    def __init__(self):
        self.reqnum = 50
        self.qps_control = threading.Semaphore(10)  # 控制每秒请求数不超过10
        self.lock = threading.Lock()  # 用于线程安全地更新进度条

    @staticmethod
    def get_img(url):
        headers = {
            'Referer': 'https://weibo.com/'
        }
        proxies = {
            'http': None,
            'https': None
        }
        response = requests.get(url=url, headers=headers)
        return response.status_code, response.url, response.content

    def download_image(self, url, file, log, pbar, thread_id):
        with self.qps_control:  # 使用信号量控制QPS
            code, geturl, content = self.get_img(url)
            # 图片文件名包含线程ID
            name = f"{int(time.time())}_{thread_id}.png"
            with open(f'./img_/{file}/{name}', "wb") as f:
                f.write(content)
            with open(log, "a") as log_file:
                log_file.write(f"code:{code} geturl:{geturl}\n")

            with self.lock:  # 确保线程安全地更新进度条
                pbar.update(1)

    def main(self):
        file = str(int(time.time()))
        if not os.path.exists(f'./img_/{file}'):
            os.makedirs(f'./img_/{file}')
        if not os.path.exists('./log/'):
            os.makedirs('./log/')

        url = "https://iw233.cn/api.php?sort=random"
        log = f'./log/{file}.log'
        threads = []

        with tqdm.tqdm(total=self.reqnum) as pbar:  # 创建进度条
            for i in range(self.reqnum):
                t = threading.Thread(target=self.download_image, args=(url, file, log, pbar, i))
                threads.append(t)
                t.start()
                time.sleep(0.1)  # 确保QPS小于10

            for t in threads:
                t.join()

if __name__ == '__main__':
    main_instance = main()
    main_instance.reqnum = 500
    main_instance.main()
