---
title: "Technical Sessions at Obertauern 2026"
description: "Technical sessions from the Obertauern 2026 Machine Learning workshop — four collaborative modules covering supervised learning, model complexity, tree methods and neural networks, and modern AI including LLMs, RAG, and agentic systems."
permalink: /courses/obertauern-2026/technical/
sidebar:
  nav: "obertauern_2026_sidebar_draft"
toc: true
toc_label: "Contents"
toc_sticky: true
---

This page outlines the structure and content of the **Technical Sessions at Obertauern 2026**, part of the Machine Learning workshop of the German Academic Scholarship Foundation. Across four 90-minute sessions, we build a conceptual arc from the foundations of supervised learning through to modern AI systems — large language models, retrieval-augmented generation, and autonomous agents. All sessions are designed for an interdisciplinary audience without requiring a mathematical background.

---

## 📚 Contents

- [Session Structure](#session-structure)
- [Session 1: Learning from Data — Classification & Evaluation](#session-1-learning-from-data--classification--evaluation)
- [Session 2: Regression & Model Complexity](#session-2-regression--model-complexity)
- [Session 3: Trees, Ensembles & Neural Networks](#session-3-trees-ensembles--neural-networks)
- [Session 4: Modern AI — Foundation Models, LLMs, RAG & Agents](#session-4-modern-ai--foundation-models-llms-rag--agents)
  - [Instructor Introduction: The Paradigm Shift & How LLMs Work](#instructor-introduction-20-minutes-the-paradigm-shift--how-llms-work)

---

## Session Structure

Sessions 1–3 follow a consistent 90-minute format:

*   **Instructor Introduction (5–10 minutes):** A brief framing of the session's themes and how they connect to previous sessions.
*   **Topic slots (60 minutes):** Four topic slots of roughly 15 minutes each — about 10 minutes for one participant to introduce a topic, followed by discussion. The focus is conceptual understanding and real-world relevance — not mathematical derivations.
*   **Discussion & Wrap-up (15–20 minutes):** Instructor-facilitated synthesis, cross-topic connections, and open questions.

**Session 4 uses a modified format.** The first two topics (the paradigm shift from classical ML to foundation models, and how LLMs work) are delivered as a single extended instructor-led introduction (~20 minutes). This ensures the conceptual foundation is solid before students build on it. Three student-led topics follow, covering what LLMs can and cannot do, retrieval-augmented generation, and agentic AI.

### Topic Slots: Collaborative Learning

Participants introduce specific sub-topics to the group, working individually or in pairs. Topics are assigned in advance to allow thorough preparation. The goal is engagement and discussion, not performance — you are simply helping your peers into the topic, not delivering a polished talk.

Each topic should end by **handing your anchor question to the room** — or another concrete question or dilemma the topic raises. The audience is expected to engage actively, not just listen: your peers will have read the same topic framing and should be ready to contribute. Aim for the last 5–10 minutes of your slot to be open conversation rather than one person talking. You don't need to resolve the question you pose — your job is to start the argument, not close it.


## Session 1: Learning from Data — Classification & Evaluation

### 1. What is ML? Classification Problems & the Confusion Matrix

*   **Core Concepts to Cover:**
    *   **What is Machine Learning?** Introduce ML as a family of methods for learning patterns from data rather than writing explicit rules. Contrast with traditional programming: instead of "if-then" logic, we show the computer examples and let it find the pattern.
    *   **Supervised Learning:** The core idea — we have inputs (features) and known outputs (labels), and we want to learn a mapping between them.
    *   **Classification:** Predicting a categorical label. Distinguish binary, multiclass, and multilabel settings with concrete examples.
    *   **The Confusion Matrix:** A table that breaks down a model's predictions into True Positives, True Negatives, False Positives, and False Negatives. Emphasise that it is the foundation for all other classification metrics — accuracy alone hides too much.

*   **Why it's Important (Interdisciplinary Focus):** Classification problems are everywhere — medical diagnosis, species identification, legal case categorisation, content moderation. The confusion matrix forces us to ask *which* mistakes the model makes, not just how often it is right. That distinction has real consequences in any applied domain.

*   **Examples to Consider:**
    *   Medical screening: is this scan positive for cancer?
    *   Ecology: does this satellite image contain a particular land-cover type?
    *   A simple 2×2 confusion matrix for a spam filter — where would you rather have your false positives?

*   **Your anchor question:** Why does a model with 99% accuracy sometimes tell us almost nothing useful?

*   **You don't need to cover:** any formulas, or how to implement a confusion matrix in code. Focus on what each cell means in plain language and why different types of mistakes carry different real-world weight.

---

### 2. Beyond Accuracy: Precision, Recall & F1-Score

*   **Core Concepts to Cover:**
    *   **Accuracy:** Proportion of correct predictions overall. Simple, but misleading when classes are imbalanced.
    *   **Precision:** Of all cases the model flagged as positive, how many actually were? Matters when false positives are costly.
    *   **Recall (Sensitivity):** Of all actual positive cases, how many did the model catch? Matters when false negatives are costly.
    *   **F1-Score:** The harmonic mean of precision and recall. A single number that balances both — particularly useful when class distributions are uneven.
    *   **The Precision-Recall Tradeoff:** Raising or lowering a decision threshold shifts the balance. There is no free lunch.

*   **Why it's Important (Interdisciplinary Focus):** The choice of metric is a values decision, not just a technical one. A cancer screening tool and a spam filter face the same mathematical tradeoff, but the human stakes are entirely different. This is one of the clearest entry points for ethical reflection on ML systems.

*   **Examples to Consider:**
    *   Rare disease screening (1 in 1000): a model that predicts "no disease" every time achieves 99.9% accuracy — and is completely useless.
    *   Contrast: for a spam filter, a few missed spam emails is tolerable; filtering a critical email is not.

*   **Your anchor question:** Why is choosing an evaluation metric a values decision, not just a technical one?

*   **You don't need to cover:** the formulas for precision, recall, or F1. If you show them on a slide, translate each one into plain English immediately. The core argument — that what you optimise for reflects what you care about — is more important than the arithmetic.

---

### 3. Robust Evaluation: ROC/AUC & Cross-Validation

*   **Core Concepts to Cover:**
    *   **Train/Test Split:** Why we can't evaluate a model on the same data it was trained on. The analogy of studying with the answer key.
    *   **Cross-Validation (k-fold):** Split data into k folds, train on k−1, test on the held-out fold, rotate, average. Gives a more reliable performance estimate than a single split.
    *   **ROC Curve:** Plots true positive rate against false positive rate across all possible thresholds. A visual summary of a model's discriminating power.
    *   **AUC (Area Under the Curve):** Summarises the ROC curve as a single number. 1.0 = perfect, 0.5 = random guessing.

*   **Why it's Important (Interdisciplinary Focus):** Scientific rigour demands that we know how well a method generalises — not just how well it fits the data we already have. Cross-validation will feel familiar to anyone who has used leave-one-out methods in ecology or statistics. AUC is especially useful for comparing models when the decision threshold isn't yet fixed.

*   **Examples to Consider:**
    *   A visual diagram of k-fold cross-validation: imagine five practice exams, each with a different subset of questions held back as the "real" test.
    *   Two ROC curves overlaid — one for a good model, one for a poor one — to show what a higher AUC looks like in practice.

*   **Your anchor question:** How do we know whether a model actually works on data it has never seen?

*   **You don't need to cover:** the mathematics behind AUC or the exact procedure for computing a ROC curve. Focus on the visual intuition and on why holding out data is non-negotiable for honest evaluation.

---

### 4. Data Quality, Sampling Bias & Why Data Beats Algorithms

*   **Core Concepts to Cover:**
    *   **Sampling Bias:** When the data used to train a model does not represent the population it will be applied to, predictions will be systematically wrong — not randomly wrong.
    *   **Non-Representative Data:** A model can only learn what the data shows it. Gaps in the data create blind spots in the model.
    *   **Feature Engineering:** Using domain knowledge to create informative inputs — transforming raw data into representations that help the model learn. This is where subject expertise matters most.
    *   **Feature Selection:** Identifying which variables actually carry predictive signal. Simpler models with well-chosen features often outperform complex models with noisy ones.

*   **Why it's Important (Interdisciplinary Focus):** The key message is that the algorithm is rarely the bottleneck. Data collection, study design, and domain expertise determine what a model can and cannot learn. For participants from fields with established data collection protocols — ecology, medicine, social science — this is the most immediately actionable insight: ML amplifies what is in the data, including its biases.

*   **Examples to Consider:**
    *   A facial recognition system trained mostly on one demographic group performs poorly on others — not because of the algorithm, but because of the training data.
    *   In ecology: a species distribution model trained only on museum specimen records will reflect where collectors went, not where the species actually lives.
    *   Feature engineering example: from a timestamp, extracting "hour of day" or "day of week" may be far more informative than the raw number.

*   **Your anchor question:** What can a machine learning model never learn, no matter how sophisticated the algorithm?

*   **You don't need to cover:** data preprocessing techniques or cleaning workflows. Focus on the conceptual argument: what the model can learn is bounded by what the data contains — not by the algorithm's intelligence.

---

## Session 2: Regression & Model Complexity

### 5. Linear Regression: Loss Functions & Loss Minimisation

*   **Core Concepts to Cover:**
    *   **What is Regression?** Predicting a continuous numerical value — price, temperature, biomass, exam score — rather than a category.
    *   **Linear Regression Intuition:** Finding the best-fit line through a scatter plot. The line summarises the relationship between input features and the output.
    *   **Residuals:** The gap between what the model predicts and what actually happened. The goal of training is to make these gaps as small as possible overall.
    *   **Loss Function (MSE):** A way of measuring total error. Mean Squared Error penalises large mistakes more than small ones. We want to minimise it.
    *   **Loss Minimisation:** Training a model means finding the parameters (slope, intercept) that minimise the loss. This is an optimisation problem — the same one that underlies neural networks, just much simpler here.

*   **Why it's Important (Interdisciplinary Focus):** Linear regression is the conceptual foundation for almost all of machine learning. The ideas of "fitting a model to data by minimising error" and "optimisation by walking downhill on a loss surface" recur throughout the course — in boosting, in neural networks, and in LLMs. Understanding it here makes everything else more coherent.

*   **Examples to Consider:**
    *   Predicting plant biomass from leaf area.
    *   Estimating income from years of education.
    *   A scatter plot showing three lines — one too steep, one too shallow, one just right — to motivate the idea of a best fit.

*   **Your anchor question:** What does it actually mean for an algorithm to "learn" from data?

*   **You don't need to cover:** matrix algebra, the normal equations, or gradient descent in detail (Session 4 revisits the optimisation idea at scale). A scatter plot with a best-fit line and the intuition of "minimising the total gap between predictions and reality" carries the whole argument.

---

### 6. Overfitting & Underfitting: The Generalisation Problem

*   **Core Concepts to Cover:**
    *   **Overfitting:** A model that has memorised the training data — including its noise — rather than learning the underlying pattern. It performs well on training data and poorly on new data.
    *   **Underfitting:** A model too simple to capture the real pattern. It performs poorly on both training and new data.
    *   **The Bias-Variance Tradeoff:** Bias is the error from a model that is too simple; variance is the error from a model too sensitive to the specific data it was trained on. Every model lives somewhere on this spectrum.
    *   **Visualising the Tradeoff:** A scatter plot with three curves — underfit, overfit, and well-fit — makes this immediately intuitive.

*   **Why it's Important (Interdisciplinary Focus):** The generalisation problem is the central challenge of machine learning. A model that works on historical data but fails on new data is not useful — and in applied fields, new data is always coming. Understanding this tradeoff helps participants think critically about published ML results: does this model actually generalise, or has it been overfit to a benchmark?

*   **Examples to Consider:**
    *   The student analogy: memorising practice exam answers (overfitting) vs. not studying enough (underfitting) vs. actually understanding the material.
    *   A visual example with polynomials of increasing degree fitted to the same scatter plot.

*   **Your anchor question:** Why is a model that perfectly explains past data often useless for predicting the future?

*   **You don't need to cover:** the mathematical decomposition of bias and variance. The visual intuition — a wiggly curve that fits every training point vs. a straight line that misses the pattern vs. a curve that captures it — makes the whole argument without any equations.

---

### 7. Regularisation: Ridge, Lasso & Early Stopping

*   **Core Concepts to Cover:**
    *   **Regularisation:** A family of techniques that prevent overfitting by penalising model complexity — encouraging the model to be simpler than the data alone would demand.
    *   **Ridge (L2):** Adds a penalty proportional to the square of the model's coefficients. Shrinks all coefficients toward zero, but keeps them non-zero.
    *   **Lasso (L1):** Adds a penalty proportional to the absolute value of coefficients. Can shrink coefficients all the way to zero — effectively performing automatic feature selection.
    *   **Early Stopping:** For iteratively trained models, stopping training before the model has fully converged to the training data. The validation loss starts rising while training loss keeps falling — that is the overfitting signal.

*   **Why it's Important (Interdisciplinary Focus):** Regularisation is the practical engineering response to the generalisation problem. The Lasso's feature selection property is especially useful in high-dimensional settings (many potential predictors, limited data) common in biology, medicine, and social science. The conceptual link to AIC/BIC model selection criteria — which penalise model complexity to prevent overfitting — will be familiar to many participants.

*   **Examples to Consider:**
    *   Lasso applied to a genomics dataset with thousands of potential gene predictors: it automatically zeroes out the uninformative ones.
    *   The analogy of a "simplicity budget": the model has to spend complexity wisely, not just fit every data point.

*   **Your anchor question:** How do you prevent a model from becoming so "clever" about past data that it fails on future data?

*   **You don't need to cover:** the penalty term formulas or how regularisation is implemented mathematically. The key intuition is: we add a cost to complexity, so the model learns to stay simple unless the data strongly justifies more. For Lasso, the practical punchline is that some variables get zeroed out entirely — the model chooses which features to ignore.

---

### 8. Feature Engineering & Feature Selection in Practice

*   **Core Concepts to Cover:**
    *   **Feature Engineering:** Creating new, more informative inputs from raw data using domain knowledge. The model can only work with what you give it — how you represent the data often matters more than which algorithm you use.
    *   **Feature Selection:** Identifying and keeping only the features that carry genuine predictive signal. Removing noise improves generalisation and makes models more interpretable.
    *   **Domain Knowledge as a Lever:** The person who understands the data and the problem is often more valuable than the person who knows the most algorithms. Feature engineering is the main channel through which expertise enters the model.

*   **Why it's Important (Interdisciplinary Focus):** This topic reframes what it means to contribute to an ML project. Participants from any field with deep domain knowledge — ecology, medicine, law, economics — can make a decisive difference in how data is prepared and which features are constructed. The best ML results in applied domains typically come from a close collaboration between domain experts and technical practitioners.

*   **Examples to Consider:**
    *   From a raw timestamp, extract hour of day, day of week, month, season — each potentially informative for different problems.
    *   In ecology: from GPS tracking data, derive movement speed, habitat type at location, and time since last rest — all potentially more predictive than raw coordinates.
    *   A side-by-side comparison: same algorithm, poor features vs. well-engineered features. The difference is often dramatic.

*   **Your anchor question:** Where does human expertise actually enter a machine learning pipeline — and why does it matter more than the choice of algorithm?

*   **You don't need to cover:** implementation details or code. The examples already in this guide — extracting hour-of-day from a timestamp, deriving movement speed from GPS coordinates — are concrete enough to anchor the whole topic without touching a line of code.

---

## Session 3: Trees, Ensembles & Neural Networks

### 9. Decision Trees → Random Forests

*   **Core Concepts to Cover:**
    *   **Decision Tree Intuition:** A series of "if-then" questions that partition the data. Highly interpretable — you can follow the tree's logic step by step. Introduce structure: root node, internal nodes, leaf nodes.
    *   **How Trees Split:** At each node, the tree finds the feature and threshold that best separates the classes or reduces prediction error. The goal is purity — groups that are as homogeneous as possible.
    *   **The Problem with a Single Tree:** A sufficiently deep tree can perfectly memorise the training data by creating a unique path for every point. It overfits severely and generalises poorly.
    *   **Random Forests:** The fix. Train many trees, each on a random subset of the data (bagging) and using only a random subset of features at each split. Average their predictions. The randomness decorrelates the trees, and averaging reduces variance dramatically.

*   **Why it's Important (Interdisciplinary Focus):** Decision trees are among the most interpretable ML models — a domain expert can inspect the logic and validate whether it makes sense. Random Forests extend this to a practical, high-performing tool. In ecology, they are widely used for species distribution modelling and land-cover classification. The key idea — that a crowd of imperfect, diverse models beats any single model — is a powerful one.

*   **Examples to Consider:**
    *   A simple decision tree for classifying whether a patient should receive treatment, showing how a domain expert could audit the logic.
    *   Random Forests for land-cover classification from satellite imagery.
    *   The "wisdom of the crowd" analogy: a diverse group of independent experts, each slightly wrong in different ways, averages out their individual errors.

*   **Your anchor question:** Why does combining many imperfect models often outperform any single well-trained one?

*   **You don't need to cover:** Gini impurity, information gain, or the mathematics of how splits are chosen. The logic of the tree structure — "ask questions to divide the data into purer groups" — and the intuition of why averaging over many diverse trees helps are the two things your peers need to walk away with.

---

### 10. Boosting & the Bias-Variance Tradeoff Revisited

*   **Core Concepts to Cover:**
    *   **Boosting:** A sequential ensemble method. Each new model is trained specifically to correct the errors of the previous ensemble. Unlike Random Forests (which build trees in parallel and average), boosting builds trees in sequence and accumulates.
    *   **Gradient Boosting (Conceptual):** The dominant modern variant. Each new tree is fitted to the residual errors of the current ensemble — it learns what the previous model got wrong.
    *   **XGBoost / LightGBM:** Name-drop these as the practical tools. They dominate tabular data competitions and are widely used in industry.
    *   **Bias-Variance Tradeoff Revisited:** Bagging/Random Forests reduce variance; boosting reduces bias. These are complementary strategies for different failure modes.

*   **Why it's Important (Interdisciplinary Focus):** Boosting algorithms are consistently among the top performers on structured/tabular data — the kind most common in scientific datasets. Understanding the conceptual distinction between bagging and boosting gives participants a mental model for why different ensemble methods exist and when to reach for each. The bias-variance framing unifies the regularisation and ensemble concepts from the previous sessions.

*   **Examples to Consider:**
    *   The study group analogy: in bagging, everyone studies independently and you average their answers; in boosting, each person focuses on the questions the group got wrong in the last round.
    *   Gradient boosting used in search ranking, ad click prediction, and clinical risk scoring.

*   **Your anchor question:** What is the difference between making many independent guesses and learning from your mistakes — and why does that distinction matter for how models are built?

*   **You don't need to cover:** the gradient boosting loss function derivation, or how XGBoost is implemented. The core distinction to convey is sequential vs. parallel: one method builds trees independently and averages, the other builds each new tree specifically to fix what the previous ones got wrong.

---

### 11. Neural Network Architecture: Layers, Neurons & Forward Propagation

*   **Core Concepts to Cover:**
    *   **High-Level Analogy:** Layers of simple processing units that transform inputs into outputs through a chain of learned transformations. Loosely inspired by biological neurons, but the analogy should not be pushed too far.
    *   **Structure:** Input layer (receives data), hidden layers (where representations are built), output layer (produces a prediction).
    *   **Activation Functions:** Non-linear "switches" applied to each neuron's output. Without them, a network of layers would collapse to a single linear transformation. ReLU (set negative values to zero) and Sigmoid (squash to 0–1) are the canonical examples.
    *   **Forward Propagation:** Data flows from input to output through a sequence of matrix multiplications and activation functions. A prediction is just the result of this forward pass.

*   **Why it's Important (Interdisciplinary Focus):** Neural networks are often treated as impenetrable black boxes. This session demystifies the basic structure. Understanding that a network is "just" a composition of simple transformations — and that its power comes from depth and non-linearity — is the conceptual foundation for everything that follows, including how LLMs work.

*   **Examples to Consider:**
    *   A clear diagram with three layers and a handful of neurons — the simplest possible visual.
    *   The dimmer-switch analogy for activation functions: not just on or off, but a continuous degree of activation.
    *   Connect back to linear regression: a single neuron with no activation function *is* linear regression. Depth and non-linearity are what make neural networks more expressive.

*   **Your anchor question:** What is actually happening inside a neural network when it produces an output — and is "black box" an accurate description?

*   **You don't need to cover:** the weight matrix mathematics or the specific functional forms of activation functions. A clear diagram and the structural logic — data flows in, gets transformed layer by layer, a prediction comes out — is everything your peers need.

---

### 12. How NNs Learn: Backpropagation, Optimisers, Dropout & Generalisation

*   **Core Concepts to Cover:**
    *   **Loss Function (Revisited):** Still measuring how wrong the model is — just now the model has millions of parameters.
    *   **Backpropagation (Conceptual):** Working backward from the output error to determine how much each weight contributed to the mistake. Think of it as distributing "blame" backward through the network. The result is a gradient — a direction to nudge each weight.
    *   **Gradient Descent & Optimisers:** We adjust weights in the direction that reduces the loss. SGD is the basic idea; Adam is the practical standard for deep learning.
    *   **Dropout:** During training, randomly deactivate a fraction of neurons. Forces the network to learn redundant representations — it can't rely on any single neuron.
    *   **Overfitting in NNs:** Large networks can easily memorise training data. Dropout, early stopping, and weight regularisation are the standard countermeasures.

*   **Why it's Important (Interdisciplinary Focus):** This session closes the loop on how learning actually happens. Backpropagation and gradient descent are the engine underneath all modern deep learning — and, at a conceptual level, also behind LLMs. Understanding that training is iterative optimisation, not magic, is the key conceptual bridge to Session 4.

*   **Examples to Consider:**
    *   The child learning to ride a bike: each fall is an error, the feedback tells them what to adjust, and over many attempts they converge on balance.
    *   Navigating a hilly landscape in the dark: gradient descent means always stepping downhill; more sophisticated optimisers have better strategies for avoiding local traps.
    *   For dropout: the team analogy — practising with random players on the bench forces everyone to be capable of covering for each other.

*   **Your anchor question:** How does a network with millions of parameters know which ones to adjust — and by how much — after making a mistake?

*   **You don't need to cover:** the chain rule or partial derivatives. The key intuition is that error flows backwards through the network to distribute "blame" across the weights, and training means iteratively nudging each weight in the direction that reduces that error. The maths formalises this; the intuition is what matters here.

---

## Session 4: Modern AI — Foundation Models, LLMs, RAG & Agents

*This session uses a modified format: an extended instructor-led introduction covers the conceptual foundations, followed by three student-led topics.*

### Instructor Introduction (~20 minutes): The Paradigm Shift & How LLMs Work

This block is delivered by the instructors as a connected narrative — not split across student-led topics — to ensure the foundation is solid before students build on it.

**From supervised learning to foundation models:**
Everything in Sessions 1–3 assumed we have labelled examples for a specific task. Foundation models break this assumption. They are pretrained on enormous amounts of unlabelled data — effectively the internet — and emerge with broad, general capabilities. Key concepts:

*   **Scale as a variable:** More data, more parameters, more compute → qualitatively different behaviour and emergent capabilities (translation, reasoning, code generation) that were not explicitly trained.
*   **Pretraining & fine-tuning:** A general model pretrained on broad data is then adapted to specific tasks with far less labelled data. A medical LLM is not built from scratch — it is a general model fine-tuned on clinical literature.
*   **What this means in practice:** You no longer need a labelled dataset for your specific task to get started. The rules of the game have shifted.

**How LLMs work (conceptual only — no maths):**

*   **What is a language model?** A model trained to predict the next token given the preceding context. Generating text is just repeated next-token prediction.
*   **Tokenisation:** Text is broken into tokens — roughly word fragments. This is how the model "sees" language.
*   **Attention:** When predicting the next word, some earlier words matter more than others. Attention is the mechanism that lets the model dynamically weight which parts of the context are most relevant. The classic example: "The trophy didn't fit in the suitcase because it was too big" — does "it" refer to the trophy or the suitcase? Humans resolve this effortlessly; attention is how the model does it.
*   **Transformers:** The architecture that makes attention practical at scale. All major LLMs use it.
*   **Autocomplete at scale:** Your phone's keyboard is a tiny language model. LLMs are the same idea, trained on orders of magnitude more data, which is why they appear to "understand."

---

### 13. What LLMs Can and Can't Do

*   **Core Concepts to Cover:**
    *   **Hallucination:** LLMs generate fluent, confident-sounding text even when they are wrong. They do not "know" facts — they predict plausible continuations of text. This is a structural property, not a bug to be patched.
    *   **Knowledge Cutoff:** The model's knowledge is frozen at its training date. It cannot know about recent events unless given that information in the prompt.
    *   **Context Window Limits:** Models can only "see" a finite amount of text at once. Very long documents, conversations, or codebases exceed this window.
    *   **Sensitivity to Phrasing:** The same question asked differently can produce substantially different answers. Output depends heavily on how the prompt is constructed.
    *   **What LLMs are genuinely good at:** Drafting, summarising, translating, reformatting, explaining, brainstorming — tasks where fluency and breadth matter more than precise factual accuracy.

*   **Why it's Important (Interdisciplinary Focus):** Critical use of LLMs requires understanding their failure modes. For participants who will use these tools in professional or research contexts — writing reports, summarising literature, extracting information from documents — knowing when to trust and when to verify is essential. This topic also sets up RAG directly: the limitations described here have partial engineering solutions, and understanding the problem makes the solution intuitive.

*   **Examples to Consider:**
    *   A legal professional asking an LLM to cite case law — it may invent plausible-sounding but non-existent citations.
    *   A researcher asking about publications from the last year — the model confidently discusses papers that don't exist.
    *   Contrast: asking an LLM to help draft an email or restructure an argument — it excels here because fluency is the goal, not factual lookup.

*   **Your anchor question:** If a language model sounds completely confident, how do you know whether to trust it?

*   **You don't need to cover:** how LLMs work technically — the instructor introduction already handles that. Focus entirely on behavioural properties: what they do reliably, where they fail in specific and predictable ways, and what that means for how you use them.

---

### 14. Retrieval-Augmented Generation (RAG)

*   **Core Concepts to Cover:**
    *   **The Core Problem:** Hallucination and knowledge cutoffs make LLMs unreliable for fact-sensitive tasks. RAG is the primary engineering response.
    *   **The RAG Solution:** At query time, retrieve relevant documents from an external knowledge base and include them in the model's context. The model then generates its answer grounded in the retrieved text.
    *   **Architecture:** Query → embed query → search a vector store for similar documents → retrieve top results → inject into prompt → generate response.
    *   **Embeddings & Similarity Search:** Documents are represented as vectors. Similar documents have similar vectors. Retrieval finds the nearest neighbours to the query vector — conceptually, finding the "closest in meaning" documents.

*   **Why it's Important (Interdisciplinary Focus):** RAG is one of the most widely deployed patterns for building reliable AI applications. It directly addresses hallucination by grounding the model in source documents you control and can verify. For participants thinking about AI tools in their own fields — a legal case database, a scientific literature assistant, a policy document analyser — RAG is the key architectural pattern to understand.

*   **Examples to Consider:**
    *   A legal assistant that retrieves relevant case law before answering a question, rather than relying on what the model may have memorised.
    *   A scientific literature tool that retrieves PubMed abstracts before summarising evidence on a clinical question.
    *   The open-book vs. closed-book exam analogy: RAG gives the model access to the relevant "book" at query time.

*   **Your anchor question:** How do you make a language model reliable enough to use in a domain where factual accuracy actually matters?

*   **You don't need to cover:** vector database implementations, embedding dimensions, or cosine similarity. The core architecture — retrieve relevant documents at query time, inject them into the prompt, generate a response grounded in that retrieved text — is the argument. The open-book exam analogy carries it.

---

### 15. Agentic AI: Agents, Memory, Planning & Tool Use

*   **Core Concepts to Cover:**
    *   **What is an Agent?** A system that uses an LLM not just to generate a single response, but to plan, take actions, observe results, and iterate — in a loop. The model decides what to do next based on what happened so far.
    *   **Tool Use:** Agents can call external tools — web search, code execution, APIs, databases — and incorporate the results. This extends what they can do far beyond text generation alone.
    *   **Memory:** Short-term (conversation context), long-term (retrieved from a database), and working memory (scratch pads within a reasoning trace).
    *   **Planning Patterns:** ReAct (Reason + Act in alternating steps) and chain-of-thought (decomposing a problem into steps before solving it) are the two most common patterns.
    *   **Multi-Agent Systems:** Multiple agents with different roles collaborating — a brief glimpse at where the field is heading.

*   **Why it's Important (Interdisciplinary Focus):** Agentic AI represents the shift from AI as a tool you query to AI as a system that acts. Understanding the basic architecture — plan, act, observe, iterate — is essential for anyone who will work with or evaluate these systems. The open questions about reliability, controllability, and accountability in agentic systems lead directly into the societal sessions.

*   **Examples to Consider:**
    *   A research assistant agent: given a question, it searches papers, extracts relevant passages, synthesises an answer, and cites its sources — all in an automated loop.
    *   A coding agent that writes code, runs it, reads the error, fixes the bug, and repeats.
    *   Multi-agent: a writing team where one agent drafts, one fact-checks, and one edits — each with a specialised role.

*   **Your anchor question:** What changes — practically and ethically — when an AI system doesn't just answer questions but takes actions in the world?

*   **You don't need to cover:** specific agent frameworks or any code. Focus on the conceptual loop — plan, act, observe, iterate — and on what becomes possible (and risky) when you add external tools and persistent memory.

---

[⬆ Back to Course Overview](/courses/obertauern-2026/) &#124; [Continue to Societal Topics ➡](/courses/obertauern-2026/societal/)
