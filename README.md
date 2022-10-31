# SlidExt
 
A Command Line tool to generate a presentation from tutorial videos where the instructor uses slides to explain the topic.
___
## Pre-requisites
1. Python 3.6 or above

## Installation
```bash
git clone https://github.com/suvanbalu/slidext.git
cd slidext
pip install -r requirements.txt
```
## Usage
```bash
python slidext.py <Sub Modules> <Arguments>
```

## Arguments
1. **Sub Module** - Video Downloader
```bash
python slidext.py vd <Arguments>
```
| Argument | Description | Default |
| --- | --- | --- |
| -l,--link | Link of the video | None |
| -s,--save | Path of Output Directory | Current Directory |
  
  
2. **Sub Module** - Slide Extractor
```bash
python slidext.py se <Arguments>
```
| Argument | Description | Default |
| --- | --- | --- |
| -s | Destination Path of the extracted images  | None |


3. **Sub Module** - PDF converter
```bash
python slidext.py pdf <Arguments>
```