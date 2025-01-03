from pyfiglet import Figlet
import sys

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 1:
        f = Figlet()
        prompt = input("Input: ").strip()
        print(f"Output:\n{f.renderText(prompt)}")
    else:
        try:
            if sys.argv[1] == '-f' or sys.argv[1] == '--font':
                f = Figlet(font=sys.argv[2])
                prompt = input("Input: ").strip()
                print(f"Output:\n{f.renderText(prompt)}")
            else:
                raise Exception
        except:
            sys.exit('Invalid usage')
else:
    sys.exit("Invalid usage")
