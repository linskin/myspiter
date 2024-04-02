from myproject.starter import run_json_spider

start_urls = [
        'https://www.jos.org.cn/jos/article/issue/2024_35_9',
        'https://www.jos.org.cn/jos/article/issue/2024_35_8',
        'https://www.jos.org.cn/jos/article/issue/2024_35_7',
        'https://www.jos.org.cn/jos/article/issue/2024_35_6',
        'https://www.jos.org.cn/jos/article/issue/2024_35_5',
        'https://www.jos.org.cn/jos/article/issue/2024_35_4',
        'https://www.jos.org.cn/jos/article/issue/2024_35_3',
        'https://www.jos.org.cn/jos/article/issue/2024_35_2',
        'https://www.jos.org.cn/jos/article/issue/2024_35_1',
    ]

run_json_spider(start_urls)