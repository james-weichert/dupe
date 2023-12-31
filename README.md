# DUPE: Detection Undermining via Prompt Engineering for Deepfake Text
#### James Weichert and Chinecherem Dimobi
CS 5914 _Fall 2023_


## README

### Data

`final_data.csv` (in the `Data/` folder) contains all 420 human and GPT-generated essays used in this research project.

#### Data Replication

The data in `final_data.csv` can be replicated using the following steps:

1. Generate GPT-written essays using the standardized prompt "Write a College \[DISCIPLINE\] class essay titled '\[TITLE\]'", replacing \[DISCIPLINE\] and \[TITLE\] with the discipline and title of the corresponding human-written essay from `human_essays.csv`, respectively. To replicate our methodology, use ChatGPT 3.5

2. Use the [ZeroGPT](https://www.zerogpt.com/) and [GPTZero](https://gptzero.me/) web interfaces to evaluate each essay (human or AI), recording the "AI GPT %" and "AI Probability" scores, respectively. This can only be done manually for ZeroGPT, but there is a GPTZero API available for purchase (although we did this step manually for GPTZero as well).

3. Paraphrase the GPT-generated essays using the desired paraphrasing prompt, then repeat step 2.

#### Watermarked Data
To regenerate the watermarked data, please use the `generate_watermark.ipynb` notebook. Once the watermarked text is generated, it is processed by the detector, which outputs the number of tokens, the number of green list tokens, and the p_values. You can find the results, including the watermarked text and its corresponding detection values, in the `watermark_detect.csv` file. For an essay to be considered as watermarked, its p_value should be greater than 0.05.

### Experiments

Most work required using web interfaces (e.g. ZeroGPT, GPTZero, ChatGPT), so the full findings are viewable in the `final_data.csv` file and cannot be programatically re-generated (see above section for replication instructions). Nevertheless, the following Python Notebooks include important Exploratory Data Analysis (EDA), supporting experiments, and the watermarking generation and detection infrastructure used for this project: 

1.  `perplexity-eda.ipynb` includes the code used for calculating the perplexity of each text, which uses [this Language Model Perplexity module](https://github.com/asahi417/lmppl#language-model-perplexity-lm-ppl). This notebook also includes the visualizations showing the distribution of perplexity scores and the relationship between perplexity and ZeroGPT "AI %" score.
2. `semantic-similarity.ipynb` includes the infrastructure for using the [Universal Sentence Encoder](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder) to generate semantic similarity scores between two texts.
3. `generate_watermark.ipynb` was used to generate the 212 watermarked GPT Neo essays.