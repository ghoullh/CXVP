# CXVP

CXVP（Chrome + Xvfb + VNC + Python） 

## Samples

* Execute Func

Open Website

```curl --location 'http://127.0.0.1:9000/browser/execute' \
--header 'Content-Type: application/json' \
--data '{
    "func": "get",
    "params": [
        "https://www.youtube.com"
    ]
}'
```

* Get Page Source

Will return HTML source of tab 0  
```
curl --location 'http://127.0.0.1:9000/browser/page/source?tab=0'
```

* Get Page Screenshot

Will return screenshot jpeg image file of the main tab
```
curl --location 'http://127.0.0.1:9000/browser/page/screenshot'
```