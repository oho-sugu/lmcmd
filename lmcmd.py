import sys
import lmstudio as lms

SERVER_API_HOST="localhost:1234"

def main():
    if len(sys.argv) < 2:
        return

    pt = sys.argv[1]

    #print(pt)

    systempt = "次のユーザーの指示を:以降の文字列に対して実行し、最もシンプルな回答のみを返答しなさい。"

    lms.configure_default_client(SERVER_API_HOST)  
    loaded_models=lms.list_loaded_models()
    model=loaded_models[0]

    sys.stdin.reconfigure(encoding='utf-8')

    for line in sys.stdin:
        #print(systempt+pt+":"+line)
        response = model.respond(systempt+pt+":"+line)
        #print(response)
        strresp = str(response)
        ind=strresp.find("<|channel|>final<|message|>")
        if ind > 0:
            print(line.rstrip() + " >> " + strresp[ind+27:].strip())

if __name__ == '__main__':
    main()
