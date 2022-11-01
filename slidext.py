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
group1.add_argument('-l','-link',type=str,action='append',help="Link(s) to Video")
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
# 
group3 = pcpdf_parser.add_mutually_exclusive_group(required=True)
group3.add_argument('-fo','-folder',help="Path of Folder")
group3.add_argument('-o','-open',help="Path of Video")
group3.add_argument('-f','-file',help="File of Links")
group3.add_argument('-l','-link',action='append',help="Link(s) to Video")
# 
pcpdf_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
pcpdf_parser.add_argument('-n','-name',default="temp.pdf",help="Name of file")


pcppt_parser=subparser.add_parser('ppt',help='PPT Converter')
# 
group4 = pcppt_parser.add_mutually_exclusive_group(required=True)
group4.add_argument('-fo','-folder',help="Path of Folder")
group4.add_argument('-o','-open',help="Path of Video")
group4.add_argument('-f','-file',help="File of Links")
group4.add_argument('-l','-link',action='append',help="Link(s) to Video")
#
pcppt_parser.add_argument('-n','-name',default="temp",help="Name of New File")
pcppt_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
pcppt_parser.add_argument('-res',default=300,help="Set resolution")
pcppt_parser.add_argument('-start',default=0,help="Starting page of PPT")
pcppt_parser.add_argument('-count',default=None,help="Page Count")
pcppt_parser.add_argument('-quiet',default=True,help="!!!!")


pc_parser=subparser.add_parser('car',help='Carousel Converter')
# 
group5 = pc_parser.add_mutually_exclusive_group(required=True)
group5.add_argument('-o','-open',help="Path of Video")
group5.add_argument('-f','-file',help="File of Links")
group5.add_argument('-l','-link',action='append',help="Link(s) to Video")
# 
pc_parser.add_argument('-s','-save',default=os.getcwd(),help="Destination of New File")
pc_parser.add_argument('-n','-name',help="Name of file")

args=parser.parse_args()
# print(args.l)

def download():
    # print(args.l)
    if args.l:
        title=videodownload.videodownload(args.s,args.l)
    else:
        title=videodownload.videodownload(args.s,filename=args.f,file=True)
    return title
try:
    if args.command=="vd":
        t=download()
        print(t)

    elif args.command=="se":
        if args.o:
            o=args.o
            slide_extractor.main(o,args.s,args.ti)
        else:
            title=download()
            for i in title:
                o=f'{args.s}\{i}.mp4'
                slide_extractor.main(o,args.s,args.ti)
                if args.nc==1:
                    array=carousel.main(args.s)
                    print(array)
                    pdf_ppt.carousel_to_pdf(array,args.s,args.s,i)
    
    elif args.command=="pdf":
        if args.fo:
            pdf_ppt.convert_to_pdf(args.fo,args.s,args.n)
        if args.o:
            o=args.o
            slide_extractor.main(o,args.s,2)
            pdf_ppt.convert_to_pdf(args.s,args.s,args.n)
        else:
            title=download()
            for i in title:
                o=f'{args.s}\{i}.mp4'
                slide_extractor.main(o,args.s,2)
                path=args.s
                pdf_ppt.convert_to_pdf(path,args.s,args.n)
                
    elif args.command=="ppt":
        if args.fo:
            pdf_ppt.convert_to_ppt(args.fo, args.s, args.n,args.res, args.start, args.count, args.quiet)
        elif args.o:
            o=args.o
            slide_extractor.main(o,args.s,2)
            pdf_ppt.convert_to_ppt(args.s, args.s, args.n, args.res, args.start, args.count, args.quiet)
        else:
            title=download()
            for i in title:
                o=f'{args.s}\{i}.mp4'
                slide_extractor.main(o,args.s,2)
                pdf_ppt.convert_to_ppt(args.s, args.s, args.n, args.res, args.start, args.count, args.quiet)

except Exception as e:
    print(e)
    print("Error/Invalid Commands")
# test/links1.txt
# C:\Users\nvnas\OneDrive\Desktop\slidext\2 Second Video.mp4
