import OS

if __name__ == '__main__':
    try:
        os.system("git pull")
        __import__("run").pil_sen()
    except Exception as e:
        exit(str(e)) 
