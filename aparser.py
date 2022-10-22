import argparse
from turtle import title
import videodownload
import slide_extractor
import Carousel.carousel as carousel
import pdf_ppt
import os


parser = argparse.ArgumentParser(description='Slide Extractor')
subparser=parser.add_subparsers(dest="command")


vd_parser=subparser.add_parser('vd',help='Video Downloader')
#
group1 = vd_parser.add_mutually_exclusive_group(required=True)
group1.add_argument('-f','-file',help="File of Links")
group1.add_argument('-l','-link',action='append',help="Link(s) to Video")
#
vd_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")


se_parser=subparser.add_parser('se',help='Slide Extractor')
#
group2 = se_parser.add_mutually_exclusive_group(required=True)
group2.add_argument('-o','-open',help="Path of Video")
group2.add_argument('-f','-file',help="File of Links")
group2.add_argument('-l','-link',action='append',help="Link(s) to Video")
#
se_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
se_parser.add_argument('-t',default=520000,help="Set threshold")
se_parser.add_argument('-ti',default=2,help="Time interval of frames in second")
se_parser.add_argument('-nc',default=1,help="No Carousel")
se_parser.add_argument('-pt',default=0,help="print thresholds") #work to be done


# conv_parser=subparser.add_parser('pc',help='PDF/PPT Converter')
# conv_parser.add_argument('-l','-path',required=True,help="Path of File")
# conv_parser.add_argument('-s','-dest',default=os.getcwd(),help="Destination of New File")

args=parser.parse_args()


def download():
    if args.l:
        title=videodownload.videodownload(args.s,args.l)
    else:
        title=videodownload.videodownload(args.s,filename=args.f,file=True)
    return title

if args.command=="vd":
    download()
elif args.command=="se":
    if args.o:
        o=args.o
    else:
        title=download()
        o=f'{args.s}\{title}.mp4'
    slide_extractor.main(o,args.s,args.t,args.ti)
    if args.nc==1:
        carousel.main()

# elif args.command=="pc":

# test/links1.txt

# C:\Users\nvnas\OneDrive\Desktop\slidext\2 Second Video.mp4