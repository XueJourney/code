import requests

def input_info():
    ms = input("请选择下载类型,若是多页下载,请输入下载的页数,默认(一页)请不输入\n")
    if ms == "":
        return 0
    else:
        return int(ms)

def get_ms(ty):
    if ty == 0:
        static_url = "https://api.codemao.cn/web/materials?filter_type=CATEGORY&offset=0&limit=30&uncollected=false&category_path=/0005&sort=LATEST_ONLINE"
        ms = requests.get(url=static_url)
        info = ms.json()
        static = info["items"]
        # print(str(static)+" \n "+str(len(static)))
    else:
        static = []
        for i in range(ty):
            static_url = "https://api.codemao.cn/web/materials?filter_type=CATEGORY&offset="+str(30*i)+"&limit=30&uncollected=false&category_path=/0005&sort=LATEST_ONLINE"
            ms = requests.get(url=static_url)
            info = ms.json()
            static = static + info["items"]
        # print(str(static)+" \n "+str(len(static)))
    print(static)
    return static,ty

def download(static,ty):
        if ty == 0:
            for i in range(len(static)):
                print("正在下载第",str(i+1),"项数据")
                res = static[i]
                print("名字:",str(res["name"]),";url:",str(res["resource_urls"][0]))
                # 下载文件
                info = requests.get(url=res["resource_urls"][0]).content
                fi = open(file="./static/"+res["name"]+".mp3",mode="+wb")
                fi.write(info)
                fi.close()
        else:
            print("一共下载",ty,"页音频")
            for i in range(ty):
                print("正在下载第",str(i+1),"页音频")
                for i in range(30):
                    print("正在下载第",str(i+1),"项数据")
                    res = static[i]
                    print("名字:",str(res["name"]),";url:",str(res["resource_urls"][0]))
                    # 下载文件
                    info = requests.get(url=res["resource_urls"][0]).content
                    fi = open(file="./static/"+res["name"]+".mp3",mode="+wb")
                    fi.write(info)
                    fi.close()
                    static.remove(static[0])

def main():
    info = input_info()
    temp = get_ms(info)
    info = temp[0]
    info2 = temp[1]
    download(info,info2)

if __name__ == "__main__":
    main()