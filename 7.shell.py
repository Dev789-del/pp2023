#Python program to emulate a UNIX/UNIX-like shell
import subprocess
Condition = True
while Condition:
    keyword = input("$ ")
    if not keyword:
        continue
    if ">" in keyword:
        outcome_auto_pop = keyword.split(">")[1].strip()
        keyword = keyword.split(">")[0].strip()
        with open(outcome_auto_pop, "w") as f:
            subprocess.run(keyword, shell = True, stdout = f)
    elif "<" in keyword:
        income_auto_pop = keyword.split("<")[1].strip()
        keyword = keyword.split("<")[0].strip()
        with open(income_auto_pop, "r") as f:
            subprocess.run(keyword, shell = True, stdin = f)
    elif "|" in keyword:
        keywords = keyword.split("|")
        p_key = None
        for command in keywords:
            command = command.strip()
            if not p_key:
                p_key = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
            else:
                p_key = subprocess.Popen(command, shell = True, stdin = p_key.stdout, stdout = subprocess.PIPE)
        print(p_key.communicate()[0].decode())
    else:
        subprocess.run(keyword, shell = True)