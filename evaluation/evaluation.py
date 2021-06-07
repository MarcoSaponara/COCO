import sys

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')   
from nltk import pos_tag
import numpy as np
from nltk.translate import bleu_score
meto = bleu_score.SmoothingFunction()
from nltk.translate.meteor_score import meteor_score

if __name__ == '__main__':
    filename = sys.argv[0]
    ref_data = sys.argv[1]
    gen_data = sys.argv[2]
    


"""
Here we read the captions and preprocess them either by tokenizing them or by
putting them in lists. We also remove sentences shorter than three words
"""
with open(ref_data, encoding='utf8') as f:
    frasi_ref = f.readlines()
frasi_ref = [el for el in frasi_ref if len(el)>2]
separate_ref = [tokenizer.tokenize(el) for el in frasi_ref]
separate_ref_pul = [el for el in separate_ref if len(el)>2]

with open(gen_data, encoding='utf8') as f:
    frasi_gen = f.readlines()
frasi_gen = [el for el in frasi_gen if len(el)>2]
separate_gen = [tokenizer.tokenize(el) for el in frasi_gen]
separate_gen_pul = [el for el in separate_gen if len(el)>2]

"""
Here we compute, in order, BLEU, Self-BLEU, POS-BLEU and METEOR
This last metric could take longer than the others to compute
"""
arr = np.array(separate_ref)
lung = arr.shape[0]
print("n captions ref =",lung)
arr_g = np.array(separate_gen)
lung_g = arr_g.shape[0]
print("n captions gen =",lung_g)

bs = np.array([bleu_score.sentence_bleu(arr,arr_g[i],smoothing_function=meto.method1)
               for i in range(lung_g)]).mean()

selfb = np.array([bleu_score.sentence_bleu(np.delete(arr_g,i),arr_g[i],smoothing_function=meto.method1) 
                  for i in range(lung_g)]).mean()

print("BLEU =",bs,"self BLEU =",selfb)

N = min(len(separate_ref_pul),len(separate_gen_pul))
sum_scores=0
for i in range(N):
    ref_pos = pos_tag(separate_ref_pul[i])
    out_pos = pos_tag(separate_gen_pul[i])
    ref_words = []
    for i in range(len(ref_pos)):
        ref_words.append(ref_pos[i][1])
    out_words = []
    for i in range(len(out_pos)):
        out_words.append(out_pos[i][1])
    score_i = bleu_score.sentence_bleu([ref_words],out_words,smoothing_function = meto.method1)
    sum_scores += score_i

print("posbleu =",sum_scores/N)

met = np.array([meteor_score(frasi_ref,el) for el in frasi_gen])

print("METEOR =",met.mean())