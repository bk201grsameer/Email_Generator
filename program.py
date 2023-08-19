import re
import fnmatch
import docx
import os

file_path = os.path.join(os.getcwd(), "template", "templates")


def list_All_The_Files(file_Path):
    try:
        file_map = {}
        files = os.listdir(file_path)
        for file in files:
            if file.endswith(".docx") and file.startswith("~") == False:
                # print(file)
                file_map[file] = os.path.join(file_path, file)
        return file_map
    except Exception as ex:
        print(ex)


def find_Templates(directory):
    docx_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, "*.docx"):
                print(os.path.join(root, file))
                docx_files.append(os.path.join(root, file))
    return docx_files


def create_Template(docx_path, file_name="random.txt"):
    try:
        doc = docx.Document(docx_path)
        # Extract the text content from the paragraphs
        docx_text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        print("[+] EMAIL FORMAT \n")
        print(docx_text)
        """ FIND ALL THE TEXTS FOR THE FORM """
        data_texts = re.findall(r"\[([^]]+)\]|\{\{([^}]+)\}\}|\(([^)]+)\)", docx_text)
        context_data = {}
        for text in data_texts:
            if (text) != "":
                if text[0]:  # text inside square brackets [ ]
                    context_data[f"[{text[0]}]"] = ""
                elif text[1]:  # text inside double curly braces {{ }}
                    stringvar = text[1]
                    output = f"{{{{stringvar}}}}"
                    context_data[output] = ""
                elif text[2]:  # text inside round brackets ( )
                    context_data[f"({text[2]})"] = ""

        print("[+] FILL IN THE DATA FOR THE CHOSEN TEMPLATE...")
        data = create_Context(context_data)

        print("[+] CREATING TEMPLATE ...")
        template_text = docx_text
        for placeholder, value in data.items():
            template_text = template_text.replace(placeholder, value)
        output_path = file_name
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(template_text)
        print("[+] Template Created..")
        print("[+] Check ", file_name)

    except Exception as ex:
        print("[-] TEMPLATE CREATION EXCEPTION ..", str(ex))


def display(mp):
    for it in mp:
        print(it, mp[it])


def create_Context(context_data):
    try:
        for it in context_data:
            context_data[it] = input(f"[+] Please Enter ${it}: ")
        return context_data
    except Exception as ex:
        print("[+] SOMETHING WENT WRONG WHILE CREATIGN CONTEXT..", str(ex))


def main():
    try:
        print("[+] APPLICATION STARTED...")
        # list all the templates
        mp = list_All_The_Files(file_path)
        i = 1
        print("[+] CHOSE TEMPLATE FROM BELOW..")
        for it in mp:
            print(f"{i}. {it}")
            i += 1

        file_name = input("[+] please Enter file name : ").strip()

        if file_name == "" or mp.get(file_name) == None:
            print("[+] Please Try again with correct data ..")
            return
        print("[+] WILL CREATE AN EMAIL TEMPLATE FOR BELOW : ", file_name)
        create_Template(mp[file_name], file_name.split(".docx")[0] + ".txt")
    except KeyboardInterrupt:
        print("[-] OPERATION CANCELLED..")


main()
