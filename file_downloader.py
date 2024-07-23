import subprocess

def download_file(uri,outputfile):
    curl_cmd = [
        "wget",
        uri
        # "--output",
        # outputfile
    ]

    try:
        subprocess.run(curl_cmd, check=True, stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
        print("Successfully Downloaded!")
    except subprocess.CalledProcessError as e:
        print("Download Failed!")


URI = input("Enter the file link you want to download: ")

download_file(URI,"output.rpm")

