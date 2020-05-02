import pandas as pd


addr = pd.read_csv('D:/stats 507/AI_risk_train_V3.0/train_recieve_addr_info1.csv')
addr['region'] = addr['region'].apply(lambda x: x[0:2] if not pd.isnull(x) else x)
region = {
	'北京': 'BJ', '天津': 'TJ', '河北': 'HE', '山西': 'SX', '内蒙': 'NM', '辽宁': 'LN',
	'吉林': 'JL', '黑龙': 'HL', '上海': 'SH', '江苏': 'JS', '浙江': 'ZJ', '安徽': 'AH',
	'福建': 'FJ', '江西': 'JX', '山东': 'SD', '河南': 'HA', '湖北': 'HB', '湖南': 'HN', 
	'广东': 'GD', '广西': 'GX', '海南': 'HI', '重庆': 'CQ', '四川': 'SC', '贵州': 'GZ',
	'云南': 'YN', '西藏': 'XZ', '陕西': 'SN', '甘肃': 'GS', '青海': 'QH', '宁夏': 'NX',
	'新疆': 'XJ', '香港': 'HK', '澳门': 'MO', '台湾': 'TW'
}

def translate(x):
	try:
		return region[x]
	except:
		if pd.isnull(x):
			return 'unknown'
		return x


addr['region'] = addr['region'].apply(translate)
addr.to_csv('D:/stats 507/AI_risk_train_V3.0/train_recieve_addr_info_eng.csv')
