import os
import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)

        with open(fileFrom, "rb") as f:
            dbx.files_upload(f.read(), fileTo, mode=WriteMode('overwrite'))


def main():
    accessToken = 'sl.BGEDcDowWegdWnrQrRsdwU3HOhFSsdXydgJNPs5LAvliuHclOFUfBZWPTIIDU5MgbGGsktznLJ6pVZ9Co99JXH14NYd5BHkgv6MENSsO47_S3qzcyWoc_KydCsHuQJgeGS7b2Gw'
    transferData = TransferData(accessToken)
    fileFrom = input('Enter the path of file : ')
    fileTo = input('Enter the path in Dropbox : ')
    for root, dirs, files in os.walk(fileFrom):

        for name in files:
            path = os.path.join(root, name)
            filePath = root.replace(fileFrom, "")
            dropboxPath = fileTo+filePath.replace("\\", "/")
            # print(dropboxPath)
            transferData.uploadFiles(path, dropboxPath)


if __name__ == '__main__':
    main()
