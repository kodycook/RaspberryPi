import codecs
import PushClient

f=codecs.open("C:\\Users\\maste\\Desktop\\test2.txt", 'r')
text = f.read()

PushClient.ConvertJson(text)
