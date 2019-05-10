import httplib2
import os
import sys
import random
import string

print('WRITE DIRECTORY NAME FOR SAVING SCREENSHOTS')
dirname = str(input())

pngCount = 0


def generate_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))


def save_pic(content, pic_id, ext):
    f = open(dirname + '/' + str(pic_id) + ext, 'wb')
    f.write(content)
    f.close


def print_status(pngCount, link, status, count):
    print(str(pngCount) + ' Screenshots Found - ' + link + status)

def abort(pngCount):
    print(' All' + '(' + str(pngCount) + ')' + ' found Screenshots were saved to: ' + os.getcwd() + '\\' + dirname + ' . Enjoy ;)')
    sys.exit(0)

print('Author: @xD4rker')
print('Press CTRL+C to abort')

if not os.path.exists(dirname):
    os.makedirs(dirname)

while True:

    try:

        status = ' BAD'
        pic_id = generate_id()
        link = 'https://prnt.sc/' + pic_id + '/direct'
        h = httplib2.Http(timeout=100)
        resp = h.request(link)

        if 'content-location' in resp[0]:
            pngUrl = resp[0]['content-location']
            ext = '.' + pngUrl[-3:]

            if (pngUrl != 'http://i.imgur.com/8tdUI8N.png') & (ext == '.png' or ext == '.jpg'):
                pngCount += 1
                save_pic(resp[1], pic_id, ext)
                status = ' OK'
        print_status(pngCount, link, status, count)
    except httplib2.RelativeURIError:
        pass
    except KeyboardInterrupt:
        abort(pngCount)
    except Exception as e:
        print('\n\n' + '[+]' + ' An error occurred: ' + str(e))
        sys.exit(1)
