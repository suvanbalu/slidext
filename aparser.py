import argparse
from asyncio.windows_events import NULL
import videodownload
import slide_extractor
import Carousel.carousel as carousel
# import pdf_ppt
import os

parser = argparse.ArgumentParser(description='Slide Extractor')

subparser=parser.add_subparsers(dest="command")

vd_parser=subparser.add_parser('vd',help='Video Downloader')
vd_parser.add_argument('-l','-link',required=True,help="Link to video")
# vd_parser.add_argument('-f','-link',required=True,help="File ")
vd_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")

se_parser=subparser.add_parser('se',help='Slide Extractor')
#
group = se_parser.add_mutually_exclusive_group(required=True)
group.add_argument('-o','-open',help="Path of Video")
group.add_argument('-l','-link',help="Link to Video")
#
se_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
se_parser.add_argument('-t',default=520000,help="Set threshold")
se_parser.add_argument('-ti',default=2,help="Time interval of frames in second")
se_parser.add_argument('-nc',default=1,help="No Carousel")
se_parser.add_argument('-pt',default=0,help='print thresholds') #work to be done

# conv_parser=subparser.add_parser('pc',help='PDF/PPT Converter')
# conv_parser.add_argument('-l','-path',required=True,help="Path of File")
# conv_parser.add_argument('-s','-dest',default=os.getcwd(),help="Destination of New File")

args=parser.parse_args()

if args.command=="vd":
    # videodownload.videodownload(args.s,args.l)
    videodownload.videodownload(args.s,filename=args.l,file=True)
elif args.command=="se":
    # if args.l!=NULL:
    #     videodownload.videodownload(args.s,filename=args.l,file=True)
    #     o=args.s
    # else:
    o=args.o
    slide_extractor.main(o,args.s,args.t,args.ti)
    if args.nc==1:
        carousel.main()

# elif args.command=="pc":


# test/links1.txt