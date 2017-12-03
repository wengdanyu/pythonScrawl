import requests
import re
import json
import os

from hashlib import md5

def parsePage(url):
	try:
		res = requests.get(url)
	except:
		print('page get wrong')
		pass
	else:
		print('ok')
		if res.status_code == 200:
			pattern = re.compile('BASE_DATA.galleryInfo = (.*?)gallery: JSON.parse\\((.*?)\\),',re.S)
			# pattern = re.compile('BASE_DATA.galleryInfo = (.*?)gallery: JSON.parse\\(\"(.*?)"\\),',re.S)
			result = re.search(pattern,res.text)
			result = result.group(2)

			data = json.loads(result)
			data = json.loads(data)

			if data and 'sub_images' in data.keys():
				for image in data['sub_images']:
					url = image['url']
					print(url)
					download_image(url)

def download_image(url):
	try:
		res = requests.get(url)
	except:
		print('download image fail')
		pass
	else:
		if res.status_code == 200:
			content = res.content
			file_path = '{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
			if not os.path.exists(file_path):
				with open(file_path,'wb') as wp:
					wp.write(content)



if __name__ =='__main__':
	url = 'https://www.toutiao.com/a6494570097976279566/'
	parsePage(url)


