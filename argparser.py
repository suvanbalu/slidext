import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
parser.add_argument('-o',type=str,help='path of video',required=True)
parser.add_argument('-s',help='destination path/current folder')

args = parser.parse_args()
print(args.accumulate(args.integers))