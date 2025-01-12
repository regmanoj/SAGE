

# **S.A.G.E: Spiritual AI-powered Gita and Enlightenment**

**S.A.G.E.** (Spiritual AI-powered Gita and Enlightenment) is an advanced AI-powered pipeline designed to retrieve relevant verses from the **Bhagavad Gita** and **Patanjali Yoga Sutras (PYS)** based on user queries. By leveraging state-of-the-art **Information Retrieval (IR)** techniques and an open-source **Large Language Model (LLM)** like **Meta-LLaMA-3.1-8B-Instruct**, this project provides contextually accurate summaries for spiritual queries. The system ensures **semantic search**, efficient **quantized models**, and **AI ethics** in handling sacred texts.

## **Core Features**
1. **Context-Aware Verse Retrieval**: Uses semantic search and ranking algorithms to identify relevant verses.
2. **LLM-Driven Summarization**: Generates concise and contextually relevant answers using an open-source LLM.
3. **Robust Query Handling**: Flags irrelevant or inappropriate queries using AI ethics considerations.
4. **Interoperable JSON Outputs**: Delivers results in structured JSON format for integration with APIs or other systems.
5. **Efficient Quantized Models**: Uses quantized models to reduce resource usage while maintaining high accuracy.
6. **Sentence Transformers**: Enhances retrieval by computing sentence embeddings for improved semantic search.

## **Project Structure**

```
project-root/
├── data/
│   ├── Bhagwad_Gita_Verses_Concepts.csv
│   ├── Bhagwad_Gita_Verses_English.csv
│   ├── Bhagwad_Gita_Verses_English_Questions.csv
│   ├── Gita_Word_Meanings_English.csv
│   ├── Gita_Word_Meanings_Hindi.csv
│   ├── Patanjali_Yoga_Sutras_Verses_English.csv
│   ├── Patanjali_Yoga_Sutras_Verses_English_Questions.csv
├── models/
│   └── Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
├── src/
│   ├── config.py       # Configuration management
│   ├── llm.py          # LLM integration for summarization
│   ├── retriever.py    # Semantic search for verse extraction
│   ├── utils.py        # Utility functions for data preprocessing
│   
├── main.py             # Entry point for executing the pipeline
├── requirements.txt    # Dependencies file
└── LICENSE             # License file
```

## **Getting Started**

### Step 1: Environment Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download and place the model**:
   Ensure the LLaMA model file (`Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf`) is placed in the `models/` directory.

### Step 2: Running the Pipeline

To start processing user queries, execute the following:

```bash
python main.py
```

### Example Query Input

Provide a query in JSON format:

```json
{
  "query": "What guidance does the Bhagavad Gita provide about karma?"
}
```

### Example Pipeline Output

```json
{
  "query": "What guidance does the Bhagavad Gita provide about karma?",
  "retrieved_verses": [
    {
      "verse": "Bhagavad Gita 2.47",
      "text": "You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions..."
    }
  ],
  "summary": "The Bhagavad Gita emphasizes performing duties with dedication while detaching oneself from the results."
}
```

## **Model and Retrieval Techniques**

### Quantized Models

- **Essence**: The project uses **quantized models**, reducing the memory and computation requirements without compromising performance. This optimization ensures the model is efficient, scalable, and capable of running on devices with lower hardware specifications, replacing traditional large models that require extensive resources.
  
### Sentence Transformers

- **Improved Semantic Search**: By integrating the **`sentence-transformers`** Python module, the retrieval process is enhanced. Sentences are embedded into high-dimensional vector space for better semantic understanding, enabling the system to retrieve the most contextually relevant verses.

---

## **AI Ethics**

AI ethics are crucial in guiding the development and deployment of **S.A.G.E.** (Spiritual AI-powered Gita and Enlightenment), a system that interacts with sacred spiritual texts such as the **Bhagavad Gita** and **Patanjali Yoga Sutras (PYS)**. Ethical principles not only ensure that the technology is used responsibly but also safeguard the values inherent in these religious and philosophical texts.

### **Key Ethical Principles:**

1. **Fairness**:
   - The system ensures that it **does not introduce bias** or **discrimination** in its interpretation of the Bhagavad Gita or PYS. Both texts are revered across different cultures, so the AI must treat every query equally, without promoting any one belief or misrepresenting the teachings. The model is designed to ensure diverse interpretations are acknowledged while keeping responses balanced and unbiased.

2. **Transparency**:
   - The AI's decision-making process is **transparent** and explainable. Each query's response is generated based on clear and traceable steps. The system pulls relevant verses from the texts and presents them with a summarized, contextually accurate response, ensuring users can easily understand how the output was derived. Furthermore, the underlying **semantic search** and **LLM summarization techniques** are documented to provide clarity on the AI's behavior.

3. **Accountability**:
   - The system is built with **auditability** in mind. Users can trace back the source of the verses that led to a given answer. Furthermore, a **query validation** mechanism ensures that inappropriate or harmful inputs are flagged and filtered. This accountability guarantees that the system is responsible for its responses and does not inadvertently spread misinformation or inappropriate content.

4. **Privacy**:
   - **User privacy** is a top priority. The system does not store or process any personal data. It only uses the query input to retrieve relevant verses and generate summaries. All interactions are kept **anonymized**, ensuring users' privacy is upheld. Additionally, any sensitive data entered is not stored beyond the session, ensuring compliance with privacy standards.

5. **Security**:
   - The system incorporates **secure coding practices** and follows standard **security protocols** to ensure it is resistant to common vulnerabilities. Furthermore, the data used (such as the Bhagavad Gita and Patanjali Yoga Sutras) is stored securely, and all communications with the system are encrypted to protect against data breaches.

6. **Human-centered**:
   - The primary goal of **S.A.G.E.** is to benefit users by providing them with **spiritual guidance** through reliable and contextual answers derived from sacred texts. The system is designed to assist users in their quest for knowledge, personal growth, and enlightenment, keeping the **human experience** at the forefront of its design. It aims to enhance the understanding of spirituality through AI while respecting the user's diverse beliefs.

7. **Societal and Environmental Well-being**:
   - The system was designed with **sustainability** in mind. By using **quantized models**, it minimizes the computational resources required, making it more efficient and environmentally friendly. The project also aims to **foster societal well-being** by providing access to spiritual wisdom, which can inspire individuals to lead better lives and promote values of peace, harmony, and self-awareness in society. The system is also structured to be scalable, so it can continue to operate in an efficient manner as the user base grows, reducing its environmental footprint.

---


## **Query and Output Validation**
The project incorporates various validation mechanisms, ensuring that queries are respectful and the outputs generated are both accurate and appropriate. These checks prevent the system from producing harmful, misleading, or culturally insensitive responses.

## **Evaluation and Performance**

### Metrics

1. **Retrieval Accuracy**: Precision of retrieved verses based on a set of curated queries.
2. **Summarization Quality**: Relevance and coherence of the generated answers.
3. **Efficiency**: Latency and resource usage per query.

### Benchmarking

- **Domain Expert Validation**: Outputs are validated for theological and contextual correctness.
- **Scalability**: Optimized to handle large datasets with minimal latency using quantized models and semantic search.

## **Future Enhancements**

1. **Multilingual Support**: Expand the retrieval and summarization capabilities to include Hindi and Sanskrit.
2. **Fine-Tuning**: Improve the LLM's performance by fine-tuning it on domain-specific datasets for more accurate summaries.
3. **Scalability**: Implement more advanced retrieval techniques to handle large-scale datasets with minimal latency.
4. **Interactive UI**: Develop a web-based or chatbot interface for better user interaction.

## **Contribution Guidelines**

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Submit a pull request with a detailed description.

## **License**

This project is licensed under the **MIT License**. Please refer to the `LICENSE` file for more details.

---

### Contact

For further inquiries or support, contact us at:regulavalasamanoj22@gmail.com.

--- 
