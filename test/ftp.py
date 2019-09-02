from pathlib import Path
from ftplib import FTP
import re

WORK_DIR = ''

def put_list_file(server, user, password, dir)
"""
    serverに .listをアップロードする

    Parameters
    ----------
    server : string
        アップロードするサーバー名。フォルダは固定
    dir : string
        アップロードするクライアント側のフォルダ

    Returns
    -------
	なし  

    """
	ftp=FTP(server)
	ftp.set_pasv("true")
	ftp.login(user, password)
	ftp.cwd('/home/tsol/list/') #ホスト側のディレクトリ


	# listファイルが残っていたら消す

	filelist = ftp.nlst(".")
	for filename in filelist
		if re.match('\.list$', filename):
		FTP.delete(filename)


	# クライアント側の .listファイルを取得してアップロード

	p = Path(WORKDIR)
	for filename in p.glob("*.list"):
		ftp.storlines("STOR " + filename, open(filename, 'rb'))

	ftp.quit()

if __name__ == '__main__':
    put_list_file('', 'tsol', 'tsol2011', WORK_DIR)
