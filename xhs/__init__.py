import requests


class XHS:
    def __init__(self):
        pass

    def get_pic_by_traceid(self, trace_id):
        pic_url = 'https://ci.xiaohongshu.com/' + trace_id + '?imageView2/2/w/0/format/jpg/v3a'
        r = requests.get(pic_url)
        with open('test.jpeg', 'wb') as jpg:
            jpg.write(r.content)


if __name__ == '__main__':
    xhs = XHS()
    # xhs.get_pic_by_traceid('1000g0082r03rerajs01g4a0t7d2k9423brt8th0')
    xhs.get_pic_by_traceid('1040g00830nfpa9r2mo005n90jel5mkkk54u2bf0')
