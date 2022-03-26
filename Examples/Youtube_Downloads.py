from pytube import YouTube # Install the required module using pip
# "pip install pytube"
# Author @codehub.py follow on instagram for more..
link = input("enter ur youtube url : ")
yt = YouTube(link)
videos = yt.streams.all()
 #this will stream all the format availabe for the video
video =list(enumerate(videos))
# this will be index all the format in list starting with zero
for i in video:
    print(i)
    # this will print all the availabe format of video with proper index
print ("enter the desired option to download the format")
dn_option = int(input(" enter the option : "))
# ask user that which format he wanted to download
dn_video = videos[dn_option]
dn_video.download() # for downloading the video
print (" downloaded successfully ")