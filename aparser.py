import argparse
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


pcpdf_parser=subparser.add_parser('pdf',help='PDF Converter')
pcpdf_parser.add_argument('-o','-open',required=True,help="Path of Video")
pcpdf_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
# 
pcppt_parser=subparser.add_parser('ppt',help='PPT Converter')
pcppt_parser.add_argument('-o','-open',required=True,help="Path of Video")
pcppt_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
pcppt_parser.add_argument('-res',default=300,help="Set threshold")
pcppt_parser.add_argument('-start',default=0,help="Starting page of PPT")
pcppt_parser.add_argument('-count',default=None,help="Page Count")
pcppt_parser.add_argument('-quiet',default=True,help="!!!!")
#
pc_parser=subparser.add_parser('car',help='Carousel Converter')
pc_parser.add_argument('-o','-open',required=True,help="Path of Video")
pc_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
pc_parser.add_argument('-n','-name',help="Name of file")
pc_parser.add_argument('-p','-pages',help="!!!!")

args=parser.parse_args()

def download():
    if args.l:
        title=videodownload.videodownload(args.s,args.l)
    else:
        title=videodownload.videodownload(args.s,filename=args.f,file=True)
    return title

if args.command=="vd":
    title=download()
    print(title)
elif args.command=="se":
    if args.o:
        o=args.o
    else:
        title=download()
        for i in title:
            o=f'{args.s}\{i}.mp4'
            slide_extractor.main(o,args.s,args.ti)
    if args.nc==1:
        carousel.main(args.s)
elif args.command=="pdf":
    pdf_ppt.convert_to_pdf(args.o,args.s,args.n)
elif args.command=="ppt":
    pdf_ppt.convert_to_ppt(args.o, args.s, args.res, args.start, args.count, args.quiet)
elif args.command=="car":
    pdf_ppt.carousel_to_pdf(args.p,args.o,args.s,args.n)


# test/links1.txt
# C:\Users\nvnas\OneDrive\Desktop\slidext\2 Second Video.mp4
