#two required procedures
#expimg http://asmodean.reverse.net/pages/expimg.html
#tlg2png https://github.com/vn-tools/tlg2png/releases
#Two programs need to be added to the Windows environment variables
#This procedure is suitable for pre-processing of CG files unpacked by Yuzu-Soft's games

import os
import subprocess
import shutil

path = 'E:\RE-BOOT\ssss'#input file path
output = 'E:\RE-BOOT\output'#output file path

pimg_files = [f for f in os.listdir(path) if f.endswith('.pimg')]
for pimg_file in pimg_files:
    input_file = os.path.join(path, pimg_file)
    subprocess.run(['expimg', input_file], shell=True)

tlg_files = [f for f in os.listdir(path) if f.endswith('.tlg')]
for tlg_file in tlg_files:
    tlg_file_path = os.path.join(path, tlg_file)
    output_file = os.path.splitext(tlg_file_path)[0] + '.png'
    output_file = os.path.join(output, os.path.basename(output_file))
    subprocess.run(['tlg2png', tlg_file_path, output_file], shell=True)

for tlg_file in tlg_files:
        tlg_file_path = os.path.join(path, tlg_file)
        os.remove(tlg_file_path)

for filename in os.listdir(path):
    if filename.endswith('.txt'):
        shutil.move(os.path.join(path,filename), output)

print('down')
