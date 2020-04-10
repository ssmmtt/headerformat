# headerformat
将Chrome开发者模式中的请求头转换为json。


复制Chrome中的请头，例如

```
:authority: ss1.bdstatic.com
:method: GET
:path: /5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/soutu/img/camera_new_x2_fb6c085.png
:scheme: https
accept: image/webp,image/apng,image/*,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8
dnt: 1
referer: https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/soutu/css/soutu.css
sec-fetch-dest: image
sec-fetch-mode: no-cors
sec-fetch-site: cross-site
user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36

```


粘贴到输入框，点击转换，会出现提示成功弹窗，该弹窗会自动消失，并将转换后的json显示出来，同时复制到剪切板。
