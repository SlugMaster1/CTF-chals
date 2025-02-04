from subprocess import run

splits = ['||','&&',';','&','|','<','>']
def validate(cmd : str):
    if '$(' in cmd: return False
    if '\\' in cmd: return False
    if cmd.count('`') > 1: return False
    if 'IFS' in cmd: return False
    if 'flag.txt' in cmd: return False
    parts = [cmd]
    for s in splits:
        nparts = []
        for l in [p.split(s) for p in parts]:
            nparts += l
        parts = nparts
    parts = [p.strip() for p in parts]
    for p in parts:
        c = p.split()[0]
        if run(['which',c],capture_output=True).stdout:
            return False
    return True
