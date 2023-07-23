import customtkinter
import platform
import psutil
import cpuinfo

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")



root = customtkinter.CTk()
root.geometry("500x500")
root.title('CompBook')
label = customtkinter.CTkLabel(root, text='CompBook for Windows')
label.pack()
label = customtkinter.CTkLabel(root, text='By Valentin Drouillet')
label.pack()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
# Infos processeurs

label = customtkinter.CTkLabel(frame, text="INFOS PROCESSEUR")
label.pack()
label = customtkinter.CTkLabel(frame, text=cpuinfo.get_cpu_info()['brand_raw'])
label.pack()
label = customtkinter.CTkLabel(frame, text="Nombres de coeurs")
label.pack()
label = customtkinter.CTkLabel(frame, text=cpuinfo.get_cpu_info()['count'])
label.pack()

ram_usage = psutil.virtual_memory().percent
# Infos RAM
def update_ram_info():
    ram_usage_label.configure(text=f"Utilisation RAM : {ram_usage}%")
    root.after(1000, update_ram_info)
ram_usage_label = customtkinter.CTkLabel(frame, text="Utilisation RAM : 0%")
ram_usage_label.pack()
update_ram_info()

root.mainloop()