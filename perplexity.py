import lmppl
import numpy as np
scorer = lmppl.LM('gpt2')

def perplexity(text, window_size=1024):

    window_perplexities = np.array([])

    for start in np.arange(0, len(text), window_size):
        
        stop = min(len(text), start + window_size)

        text_slice = text[start: stop]

        ppl = scorer.get_perplexity(text_slice)

        window_perplexities = np.append(window_perplexities, ppl)

    return np.mean(window_perplexities)