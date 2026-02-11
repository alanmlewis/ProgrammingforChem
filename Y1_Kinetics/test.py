necessary_packages=['datetime','pathlib','csv','numpy','sys','os','matplotlib','glob','scipy','pandas','inspect']
optional_packages=['serial','sklearn']

success = True
for pkg in necessary_packages:
    try:
        __import__(pkg)
        print(pkg+" imported")
    except:
        print(pkg + " not found. Please ask for help!")
        success = False

for pkg in optional_packages:
    try:
        __import__(pkg)
        print(pkg+" imported")
    except:
        print(pkg + " not found. This is only needed for advanced problems, and your setup is probably fine.")

if success: print("Success: All required python libraries are present.")
