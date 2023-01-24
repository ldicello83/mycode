#!/usr/bin/end python3
# Import additional code to complete our task
import shutil
import os

def main():
    """code to move files around"""
    os.chdir("/home/student/mycode/")

    # Copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy entire dir

    os.system("rm -rf /home/student/mycode/5g_research_backup/")

    # Copy entire directory
    shutil.copytree("5g_research/", "5g_research_backup/")
if __name__ == " __main__":
    main()
