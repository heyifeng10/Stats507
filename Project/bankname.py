import pandas as pd


bank = pd.read_csv('D:/stats 507/AI_risk_train_V3.0/train_bankcard_info1.csv')
bank_name = {'中信银行': 'citic', '工商银行': 'icbc', '中国邮政': 'post', '招商银行': 'cmb', '中国银行': 'boc', '民生银行': 'cmbc',
			'广发银行': 'gdb', '交通银行': 'bcom', '中国交通银行': 'bcom', '建设银行': 'ccb', '北京银行': 'bob', '平安银行': 'pab',
			'光大银行': 'ceb', '兴业银行': 'cib', '浦发银行': 'spdb', '华夏银行': 'hxb', '江苏银行': 'jsb', '东莞农村商业银行': 'drcb',
			'河北省农村信用社': 'hbnx', '深圳农村商业银行': 'szrcb', '龙江银行': 'bolj', '浙江泰隆银行': 'zjtlcb', '广西农村信用社': 'gxnx',
			'江苏农村商业银行': 'jsnx', '湖南农村信用社': 'hunnx', '汉口银行': 'hkb', '北京农商行': 'bjrcb', '济宁银行': 'bojn',
			'深圳发展银行': 'sdb', '河南省信用社': 'hnnx', '上海农商行': 'srcb', '重庆农商行': 'cqrcb', '盛京银行': 'bosj', '吉林省农村信用社': 'jlnx',
			'广州农商行': 'grcb', '徽商银行': 'hsb', '四川省农村信用社': 'scnx', '浙商银行': 'czb', '杭州银行': 'hzb', '宁波银行': 'nbcb',
			'云南省农村农信社': 'ynnx', '包商银行': 'bsb', '海南省农村信用社': 'hnrcc', '贵阳银行': 'bogy', '黑龙江农村信用社': 'hljnx',
			'湖北银行': 'hbcl', '南京银行': 'njcb', '南昌银行': 'bonc', '营口银行': 'boyk', '晋中银行': 'jzcb', '张家港农商银行': 'zjgrcb',
			'内蒙古农村信用社': 'nmgnx', '陕西省农村信用社': 'shxnx', '厦门银行': 'boxm', '吉林银行': 'bojl', '长安银行': 'chab', '桂林银行': 'bogl',
			'临商银行': 'lsb', '广州市农村信用社': 'gzrcc', '温州银行': 'wzcb', '湖北省农村信用社': 'hubnx', '日照银行': 'rzb', '甘肃省农村信用社': 'gsnx',
			'哈尔滨银行': 'bohrb', '华融湘江银行': 'boxj', '兰州银行': 'lzcb', '青岛银行': 'qdccb', '锦州银行': 'jzb', '昆山农商银行': 'ksrcb',
			'台州银行': 'botz', '农业银行': 'abc', '青海省农村信用社': 'qhnx', '上海银行': 'shb', '九江银行': 'jjccb', '贵州省农村信用社': 'gznx',
			'恒丰银行': 'egb', '成都农商银行': 'cdrcb', '西安银行': 'boxa', '成都银行': 'bocd', '中国光大银行': 'ceb', '中国民生银行': 'cmbc',
			'云南省农村信用社': 'ynnx', '北京农村商业银行': 'bjrcb', '广州农村商业银行': 'grcb', '河南省农村信用社': 'hnnx', '重庆农村商业银行': 'cqrcb',
			'黑龙江农信': 'hljnx', '上海农村商业银行': 'srcb', '渤海银行': 'cbhb', '顺德农商银行': 'sdeb', '微众银行': 'webank', '邮政储蓄': 'post',
			'韩亚银行': 'hanabank', '浙江农信银行': 'zjnx', '中原银行': 'zyb', '天津滨海农村商业银行': 'tjrcb', '天津农商银行': 'tjrcb', '储蓄卡': 'debit', '信用卡': 'credit'}

def translate(x):
	try:
		return bank_name[x]
	except:
		if pd.isnull(x):
			return 'unknown'
		return x

bank['bank_name'] = bank['bank_name'].apply(translate)
bank['card_type'] = bank['card_type'].apply(translate)
bank.to_csv('D:/stats 507/AI_risk_train_V3.0/train_bankcard_info_eng.csv')