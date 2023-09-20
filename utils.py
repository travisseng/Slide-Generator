
def dict2markdown(dictio):
    output = []
    blocks = {"header","body", "footer"}

    for section in dictio:
        # print("section" + str(section))
        for el in section:
            for cnt in section[el]:
                print(cnt)
                if "title" in cnt.keys():
                    output.append("# %s" % cnt["title"])
                elif "text" in cnt.keys():
                    output.append(cnt["text"])
                else:
                    output.append("<%s>" % list(cnt.keys())[0])
        output.append("---")
    return "\n\n".join(output[:-1])

