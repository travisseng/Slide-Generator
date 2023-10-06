import glob
import tqdm
import json
slide_from_wikipedia = sorted(glob.glob("Wikipedia/*/slide.json"))
print(len(slide_from_wikipedia))

## load summarize model
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# model_name_or_path = "TheBloke/Mistral-7B-Instruct-v0.1-GPTQ"
# # To use a different branch, change revision
# # For example: revision="gptq-4bit-32g-actorder_True"
# model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
#                                              device_map="auto",
#                                              trust_remote_code=False,
#                                              revision="main")

# tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

from llama_cpp import Llama
llm = Llama(model_path="../llama.cpp/mistral-7b-instruct-v0.1.Q5_K_M.gguf", n_ctx=16000, n_gpu_layers=1000)

unwanted = {"External links", "References", "See also", "Further reading", "Contents", "Foonotes"}

for sli in tqdm.tqdm(slide_from_wikipedia):
    with open(sli, "r") as json_f:
        slide1 = json.load(json_f)
    contents = slide1[1:]
    # for i,c in enumerate(contents):
    #     title_to_id[c["title"].lower()] = i

    
    article_name = sli.split("/")[-2]
    titles = [c["title"] for c in contents if c["title"] not in unwanted]
    # prompt = "Create a slide presentation about {} with the following slide titles: {}.".format(article_name, ",".join(titles))
    sli_titles = ",".join(titles)
    # print(sli_titles)
    prompt = "Give me a quite detailed slide presentation about %s with the following slide titles: %s." % (article_name, sli_titles)
    prompt_template=f'''<s>[INST] {prompt} [/INST]'''
    # print(prompt)

    # print("\n\n*** Generate:")  

    # input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
    # # output = model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=2048)
    # output = model.generate(inputs=input_ids, do_sample=False, num_beams=2, max_new_tokens=8126)
    # with open("Wikipedia/%s/output_sum.txt" % articl  e_name, "w") as f:
    #     f.write(tokenizer.decode(output[0]))
    output = llm(prompt_template, max_tokens=16000, top_k=1, top_p=0, echo=True)
    # print(output)
    with open("Wikipedia/%s/output_sum.txt" % article_name, "w") as f:
        f.write(output["choices"][0]["text"])

# print(output)