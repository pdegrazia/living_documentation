envs = {
	'QA': {'repo': 'git@github.com:workshare/qa.git',
			'image_path': './images/Logo-with-strapline_Black-400.png',
			'test_dir': './QA/FeatureTest/suites/regression/',
			'file_type': '*.txt',
			'file_pattern': ['[0-9]*.txt', 'WEB*.txt']
			},
	'ALPACA': {'repo': 'git@github.com:workshare/alpaca.git',
				'image_path': './images/workshare_transact.png',
				'test_dir': './ALPACA/qa/FeatureTest/suites/regression/',
				'file_type': '*.robot',
				'file_pattern': []
				},
	'COMPARE': {'repo': 'git@github.com:workshare/compare-server-qa.git',
				'image_path': './images/workshare_transact.png',
				'test_dir': './COMPARE/FeatureTest/suites/',
				'file_type': '*.robot',
				'file_pattern': []
				},
	'DELTA': {'repo': 'git@github.com:workshare/deltaviewqa.git',
				'image_path': './images/deltaview.png',
				'test_dir': './DELTA/FeatureTest/Suites/',
				'file_type': '*.txt',
				'file_pattern': ['Compare*', 'Deltaview*', 'Get*', 'Swap*']
				},
}
