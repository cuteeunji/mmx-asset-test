import os
from mmxlib.s3a import s3downloader

os.environ['BUCKET_NAME'] = 's3-an2-ha-linearcomp-cw2'
os.environ['INDEX_CODE'] = 'category=anomaly/type=raw/item=align_min/'

home = os.environ['project_home']
dest_path = os.path.join(home, 'data_in')
start_time = '2021-11-01T00:00:00'
end_time = '2021-11-01T00:30:00'

s3 = s3downloader.S3Downloader(dest_path, start_time, end_time, '')
s3.execute()
