import os
import subprocess

path = r'C:\Users\hukin\Desktop\cc'
output = r'C:\Users\hukin\Desktop\out'

tlg_files = [f for f in os.listdir(path) if f.endswith('.tlg')]
for tlg_file in tlg_files:
    tlg_file_path = os.path.join(path, tlg_file)
    output_file = os.path.splitext(tlg_file_path)[0] + '.png'
    output_file = os.path.join(output, os.path.basename(output_file))
    subprocess.run(['tlg2png', tlg_file_path, output_file], shell=True)