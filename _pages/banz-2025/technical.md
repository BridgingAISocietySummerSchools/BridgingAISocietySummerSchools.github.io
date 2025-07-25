---
title: "Technical Sessions"
layout: single
permalink: /banz-2025/technical/
classes: wide
---

This page outlines the structure and content of the four technical sessions in our *Machine Learning for Interdisciplinary Audiences* course. Each session covers a major area of machine learning and is built around collaborative, discussion-based learning.

---

## 📚 Contents

- [Session Structure](#session-structure)
- [Core Concepts Covered](#core-concepts-covered)
- [Session 1: Classification](#session-1-classification)
- [Session 2: Regression](#session-2-regression)
- [Session 3: Tree-based Methods & Ensembles](#session-3-tree-based-methods--ensembles)
- [Session 4: Neural Networks](#session-4-neural-networks)

---

## Session Structure

Each 75-minute topical technical session follows a consistent structure:

*   **Instructor Introduction (5-10 minutes):** Each session begins with a brief overview by the instructors to introduce the main themes and set context.
*   **Mini-Presentations (45-60 minutes):** The core interactive component, delivered by participants.
*   **Discussion/Clarification Blocks:** Interspersed throughout or at the end, facilitated by the course instructors.
*   **Wrap-up & Discussion (10-15 minutes):** Synthesizes learnings and connects concepts to real-world applications.

### Mini-Presentations: Collaborative Learning

To foster interactive learning and deeper engagement, participants will deliver short mini-presentations on specific sub-topics within each thematic session. These presentations are designed to be 10-15 minutes long, focusing on conceptual understanding and practical implications rather than complex mathematical derivations. Participants will work in pairs or individually, with topics assigned in advance to ensure comprehensive coverage and allow for thorough preparation.

## Core Concepts Covered

The course delves into the following core Machine Learning paradigms:

*   **Classification:** Predicting categorical outcomes.
*   **Regression:** Predicting continuous numerical values.
*   **Tree-based Methods & Ensembles:** Leveraging decision trees and combining multiple models for improved performance.
*   **Neural Networks:** Understanding the fundamentals of deep learning architectures.

[⬅ Back to Course Overview](/banz-2025/) &#124; [⬆ Back to top](#)


## Session 1: Classification

### 1. Classification Problem Types & Confusion Matrix

*   **Core Concepts to Cover:**
    *   **What is Classification?** Explain it as a machine learning task where the goal is to predict a categorical label or class for a given input. Contrast it with regression (predicting continuous values).
    *   **Binary Classification:** Problems with two possible outcomes (e.g., spam/not spam, disease/no disease).
    *   **Multiclass Classification:** Problems with more than two mutually exclusive outcomes (e.g., classifying animal species, types of news articles).
    *   **Multilabel Classification:** Problems where an instance can belong to multiple categories simultaneously (e.g., tagging an image with multiple objects present, assigning multiple genres to a movie).
    *   **The Confusion Matrix:** Explain this as a table that summarizes the performance of a classification model. Define its components: True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN). Emphasize that it's the foundation for understanding where a model makes mistakes.

*   **Why it's Important (Interdisciplinary Focus):** Classification is ubiquitous across disciplines. Understanding the different types of classification problems helps frame real-world challenges. The Confusion Matrix is crucial because it moves beyond a simple accuracy score and allows for a nuanced understanding of model errors, which is critical for decision-making in fields like medicine, finance, and social sciences.

*   **Examples to Consider:**
    *   **Binary:** Medical diagnosis (cancer/no cancer), loan default prediction (default/no default).
    *   **Multiclass:** Image recognition (cat/dog/bird), sentiment analysis (positive/negative/neutral).
    *   **Multilabel:** Content tagging (news article about politics, economy, technology).
    *   **Confusion Matrix:** Illustrate with a simple example, perhaps from a medical test or spam filter, showing how TP, TN, FP, FN are counted and what they mean in that context.

### 2. Key Classification Metrics

*   **Core Concepts to Cover:**
    *   **Accuracy:** The proportion of correctly classified instances (TP + TN) / Total. Explain its simplicity but also its limitations, especially with imbalanced datasets.
    *   **Precision (Positive Predictive Value):** Of all instances predicted as positive, how many were actually positive (TP / (TP + FP)). Emphasize its importance when the cost of False Positives is high.
    *   **Recall (Sensitivity or True Positive Rate):** Of all actual positive instances, how many were correctly identified (TP / (TP + FN)). Emphasize its importance when the cost of False Negatives is high.
    *   **F1-Score:** The harmonic mean of Precision and Recall. Explain it as a single metric that balances both, particularly useful when there's an uneven class distribution.

*   **Why it's Important (Interdisciplinary Focus):** Different metrics highlight different aspects of model performance, and the choice of which metric to prioritize depends heavily on the specific problem and its real-world consequences. This is a critical concept for anyone applying ML in their field.

*   **Examples to Consider:**
    *   **Precision vs. Recall:** Contrast a spam filter (high precision is important to avoid missing important emails) with a medical screening test (high recall is crucial to avoid missing actual cases of disease).
    *   **Accuracy Limitation:** Use an example of a rare disease (e.g., 1 in 1000 people have it). A model that always predicts 'no disease' would have 99.9% accuracy but would be useless. This highlights the need for other metrics.

### 3. Robust Evaluation

*   **Core Concepts to Cover:**
    *   **ROC Curves (Receiver Operating Characteristic):** Explain this as a graph that shows the performance of a classification model at all classification thresholds. It plots the True Positive Rate (Recall) against the False Positive Rate.
    *   **AUC (Area Under the ROC Curve):** Describe this as a single number that summarizes the ROC curve. An AUC of 1.0 represents a perfect model, while an AUC of 0.5 represents a model with no discriminative power (like a random guess).
    *   **Cross-Validation:** Explain this as a technique for assessing how the results of a statistical analysis will generalize to an independent data set. Describe the basic idea of k-fold cross-validation: splitting the data into 'k' subsets, training on k-1 subsets, and testing on the remaining one, then repeating this process 'k' times and averaging the results.

*   **Why it's Important (Interdisciplinary Focus):** These techniques provide a more robust and reliable assessment of a model's performance. ROC/AUC are particularly useful for comparing models and for dealing with imbalanced datasets, which are common in many fields. Cross-validation is the gold standard for ensuring that a model's performance is not just a fluke of a particular data split, which is crucial for scientific rigor and building trust in ML models.

*   **Examples to Consider:**
    *   **ROC/AUC:** Show a visual example of two ROC curves, one for a good model and one for a poor one, to illustrate how AUC helps in model selection.
    *   **Cross-Validation:** Use a simple diagram to explain how k-fold cross-validation works. You can use an analogy like having multiple practice exams to get a better sense of your true knowledge, rather than just one.

[⬅ Back to Course Overview](/banz-2025/) &#124; [⬆ Back to top](#)


## Session 2: Regression

### 4. Linear Regression Fundamentals & Loss Minimization

*   **Core Concepts to Cover:**
    *   **What is Regression?** Explain it as a machine learning task where the goal is to predict a continuous numerical value (e.g., price, temperature, age).
    *   **Linear Regression Intuition:** Describe this as finding the 'best-fit' straight line (or plane) that describes the relationship between input features and the output value. Use a simple 2D scatter plot to illustrate this.
    *   **Loss Function:** Introduce this as a way to measure how well the model's predictions match the actual data. Explain the concept of 'residuals' (the errors between the predicted and actual values). You can mention Mean Squared Error (MSE) as a common loss function without going into the formula in detail.
    *   **Loss Minimization:** Explain that the goal of training is to find the model parameters (the slope and intercept of the line) that minimize the loss function. This is the core idea of optimization in machine learning.

*   **Why it's Important (Interdisciplinary Focus):** Linear regression is the foundational model for understanding how supervised learning works. The concepts of a loss function and loss minimization are universal across almost all machine learning models, including complex neural networks. Understanding this simple case provides a strong foundation for all subsequent topics.

*   **Examples to Consider:**
    *   Predicting house prices based on square footage.
    *   Estimating a student's exam score based on hours studied.
    *   Forecasting sales based on advertising spend.

### 5. Overfitting, Underfitting, & Regularization

*   **Core Concepts to Cover:**
    *   **Overfitting:** Explain this as a model that learns the training data too well, including its noise and random fluctuations. Such a model performs poorly on new, unseen data. Use an analogy like a student who memorizes the answers to a practice exam but can't answer new questions.
    *   **Underfitting:** Explain this as a model that is too simple to capture the underlying patterns in the data. It performs poorly on both the training and new data. The analogy would be a student who hasn't studied enough.
    *   **Regularization:** Introduce this as a set of techniques used to prevent overfitting by adding a penalty for model complexity. Explain the conceptual difference between Ridge (L2) and Lasso (L1) regularization: Ridge shrinks coefficients, while Lasso can shrink them to zero, effectively performing feature selection. You don't need to show the formulas, just the conceptual idea.
    *   **Early Stopping:** Briefly explain this as a practical regularization technique where you stop training the model when its performance on a validation set starts to degrade.

*   **Why it's Important (Interdisciplinary Focus):** The tradeoff between overfitting and underfitting is the central challenge in all of machine learning. Understanding this concept is crucial for building models that are not just accurate on past data but are also useful for making predictions on new data. Regularization provides practical tools to manage this tradeoff, which is essential for building robust and reliable models in any field.

*   **Examples to Consider:**
    *   **Overfitting/Underfitting:** Show a visual example with a scatter plot and three lines: one underfitting, one overfitting (wiggly), and one that is a good fit.
    *   **Regularization:** Use an analogy like a 'simplicity budget' for a model. Regularization forces the model to be more 'frugal' with its complexity.

### 6. Data Quality & Feature Impact

*   **Core Concepts to Cover:**
    *   **Sampling Bias & Non-Representative Data:** Explain how data that is not representative of the real-world population can lead to biased and unfair models. Use clear examples to illustrate this.
    *   **Feature Engineering:** Describe this as the process of using domain knowledge to create new features from existing data that can improve model performance. It's about making the data more informative for the model.
    *   **Feature Selection:** Explain this as the process of selecting the most relevant features from the data to use in a model. This can improve model performance, reduce overfitting, and make the model more interpretable.

*   **Why it's Important (Interdisciplinary Focus):** This topic emphasizes that machine learning is not just about algorithms; the quality and preparation of data are often more important. For an interdisciplinary audience, this is a key takeaway, as it highlights the crucial role of domain expertise in building effective and responsible ML models. It connects the technical aspects of ML to the real-world context of data collection and understanding.

*   **Examples to Consider:**
    *   **Sampling Bias:** A facial recognition system trained primarily on images of one demographic group may perform poorly on others.
    *   **Feature Engineering:** From a 'date' column, you could create features like 'day of the week' or 'month', which might be more predictive.
    *   **Feature Selection:** In a medical diagnosis model, you might find that only a few key measurements are actually predictive of a disease, and you can build a simpler, more interpretable model by focusing on them.

[⬅ Back to Course Overview](/banz-2025/) &#124; [⬆ Back to top](#)


## Session 3: Tree-based Methods & Ensembles

### 7. Decision Trees: Structure, Splitting & Overfitting

*   **Core Concepts to Cover:**
    *   **Decision Tree Intuition:** Explain decision trees as a series of 'if-then-else' questions that lead to a decision. They are highly interpretable and mimic human decision-making.
    *   **Structure:** Describe the components of a decision tree: root node, internal nodes (decision nodes), and leaf nodes (terminal nodes).
    *   **Splitting:** Conceptually explain how a tree learns by finding the best feature to split the data at each node to make the resulting groups as 'pure' as possible. You can mention Gini impurity or entropy as measures of impurity without going into the math.
    *   **Overfitting in Trees:** Explain why a single, deep decision tree is prone to overfitting. It can create a unique path for every single data point in the training set, making it unable to generalize.

*   **Why it's Important (Interdisciplinary Focus):** Decision trees are one of the most intuitive and interpretable machine learning models. For an interdisciplinary audience, their transparency is a huge advantage, as it allows domain experts to understand and validate the model's logic. Understanding their limitations (overfitting) is crucial for appreciating why more complex ensemble methods are often necessary.

*   **Examples to Consider:**
    *   A simple decision tree for deciding whether to play tennis based on weather conditions.
    *   A medical diagnosis tree that asks a series of questions about symptoms to arrive at a possible diagnosis.

### 8. Bagging & Random Forests

*   **Core Concepts to Cover:**
    *   **Ensemble Learning:** Introduce the concept of combining multiple models to achieve better performance than any single model. Use the analogy of asking a diverse group of experts for their opinion rather than just one.
    *   **Bagging (Bootstrap Aggregating):** Explain this as a technique where you create multiple random subsets of the training data (with replacement), train a separate model on each subset, and then average their predictions. This reduces variance and makes the model more stable.
    *   **Random Forests:** Describe this as an extension of bagging where, in addition to sampling the data, you also sample the features at each split in each tree. This 'de-correlates' the trees and makes the ensemble even more powerful.

*   **Why it's Important (Interdisciplinary Focus):** Random Forests are one of the most widely used and effective machine learning algorithms. They are robust, handle a variety of data types, and are less prone to overfitting than single decision trees. For an interdisciplinary audience, they represent a powerful, off-the-shelf tool that often provides excellent results with less tuning than other complex models.

*   **Examples to Consider:**
    *   Use the 'wisdom of the crowd' analogy for ensemble learning.
    *   Explain how Random Forests are used in fields like ecology (e.g., classifying land cover from satellite images) or finance (e.g., predicting credit risk).

### 9. Boosting & The Bias-Variance Tradeoff

*   **Core Concepts to Cover:**
    *   **Boosting:** Explain this as a sequential ensemble method where each new model is trained to correct the errors of the previous ones. It's like a team of specialists where each member focuses on the mistakes made by the one before them.
    *   **Gradient Boosting (Conceptual):** Describe this as a popular and powerful type of boosting. You don't need to explain the 'gradient' part in detail, but you can say that it works by fitting new models to the 'residual errors' of the previous ensemble.
    *   **The Bias-Variance Tradeoff:** Revisit this fundamental concept. Explain that bias is the error from overly simplistic assumptions, while variance is the error from being too sensitive to the training data. Use a visual analogy like darts on a target to explain high/low bias and variance.
    *   **How Ensembles Manage the Tradeoff:** Explain that bagging/Random Forests primarily reduce variance, while boosting primarily reduces bias.

*   **Why it's Important (Interdisciplinary Focus):** Boosting algorithms are often the top performers in machine learning competitions and are widely used in industry. Understanding the conceptual difference between bagging and boosting provides a deeper insight into how ensemble methods work. The bias-variance tradeoff is arguably the most important concept in classical machine learning, and understanding it is crucial for diagnosing model problems and choosing appropriate strategies for improvement.

*   **Examples to Consider:**
    *   Use the analogy of a group of students studying for an exam: bagging is like having each student study independently and then averaging their answers, while boosting is like having them study together, with each student focusing on the topics the others found difficult.
    *   Discuss how boosting is used in search ranking or ad recommendation systems.

[⬅ Back to Course Overview](/banz-2025/) &#124; [⬆ Back to top](#)


## Session 4: Neural Networks

### 10. Neural Network Fundamentals

*   **Core Concepts to Cover:**
    *   **Basic Analogy:** Start with a very high-level analogy to the brain's neurons and connections.
    *   **Structure:** Explain the basic components: input layer (where data comes in), hidden layers (where the 'magic' happens), and output layer (where the prediction comes out). Describe neurons (or nodes) as the basic processing units.
    *   **Activation Functions:** Explain these as the 'on/off' switches for neurons. They introduce non-linearity, which is what allows neural networks to learn complex patterns that linear models cannot. Mention common examples like ReLU and Sigmoid conceptually.
    *   **Forward Propagation:** Describe this as the process of data flowing through the network from the input layer to the output layer to make a prediction. It's a one-way street of calculations.

*   **Why it's Important (Interdisciplinary Focus):** This topic demystifies the basic structure and operation of neural networks, which are often seen as 'black boxes'. For an interdisciplinary audience, understanding these fundamental building blocks is the first step to appreciating how these powerful models work and what makes them different from the models discussed in previous sessions.

*   **Examples to Consider:**
    *   Use a very simple visual diagram of a neural network with a few neurons and layers.
    *   For activation functions, use an analogy like a dimmer switch for a light bulb – it's not just on or off, but can have different levels of activation.

### 11. Neural Network Learning

*   **Core Concepts to Cover:**
    *   **Loss Function:** Revisit this concept. It's a measure of how wrong the network's predictions are.
    *   **Backpropagation (Conceptual):** Explain this as the process of working backward from the error to figure out how much each connection in the network contributed to it. It's like assigning blame for the error. This 'blame' information is then used to update the connections.
    *   **Optimizers (Conceptual):** Describe these as the algorithms that guide the process of updating the network's connections (weights) to reduce the error. Mention Stochastic Gradient Descent (SGD) as the basic idea of taking small steps 'downhill' on the error surface, and Adam as a more advanced, adaptive optimizer that is often used in practice.

*   **Why it's Important (Interdisciplinary Focus):** This topic explains the 'learning' part of deep learning. Understanding that neural networks learn by iteratively adjusting their internal connections to minimize error is a core concept. For an interdisciplinary audience, it's crucial to grasp that this is a process of optimization, similar to what was discussed in the context of linear regression, but on a much larger scale.

*   **Examples to Consider:**
    *   Use the analogy of a child learning to ride a bike: they make a mistake (error), get feedback, and adjust their posture and balance (update weights) to do better next time.
    *   For optimizers, you can use the analogy of trying to find the lowest point in a hilly landscape in the dark. SGD is like taking a step in the steepest downward direction, while more advanced optimizers are like having a better strategy for navigating the terrain.

### 12. Regularization in Neural Networks

*   **Core Concepts to Cover:**
    *   **Overfitting in Neural Networks:** Explain why large neural networks are particularly prone to overfitting – they have so many parameters that they can easily memorize the training data.
    *   **Dropout:** Describe this as a technique where, during training, you randomly 'turn off' a fraction of the neurons in the network. This forces the network to learn more robust and redundant representations, as it can't rely on any single neuron.
    *   **Batch Normalization:** Conceptually explain this as a technique that helps stabilize and speed up the training process by normalizing the inputs to each layer. It has a regularizing effect as a side benefit.

*   **Why it's Important (Interdisciplinary Focus):** Regularization is absolutely essential for building effective deep learning models. Without it, most neural networks would be useless due to overfitting. For an interdisciplinary audience, understanding these techniques highlights the practical engineering and 'tricks of the trade' that are necessary to make deep learning work in the real world. It shows that building these models is not just about designing an architecture, but also about carefully managing the training process.

*   **Examples to Consider:**
    *   For Dropout, use the analogy of training a team where you randomly send some players to the bench during practice. This forces the remaining players to learn to work together in different combinations and not rely on any single star player.
    *   For Batch Normalization, you can use a high-level analogy of 're-centering' the conversation in a group discussion to keep everyone on the same page, which makes the discussion more efficient.

---

[⬅ Back to Course Overview](/banz-2025/) &#124; [⬆ Back to top](#)
