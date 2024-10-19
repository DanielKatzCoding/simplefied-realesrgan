import subprocess


def run(command: str, void=False):
    try:
        if void:
            subprocess.run(command, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        return {"log": {"error": f"An error occurred: {e}"}}
    except Exception as e:
        return {"log": {"error": f"An unexpected error occurred: {e}"}, "run-state": '1'}
