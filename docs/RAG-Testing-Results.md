# ElectroHelp AI – RAG Testing Results

## 1. Project Information

| Item | Details |
|---|---|
| Project | ElectroHelp AI |
| Project Type | Generative AI Customer Support Chatbot |
| Testing Area | Retrieval-Augmented Generation (RAG) |
| Backend | Python and FastAPI |
| Language Model | Groq – GPT-OSS-20B |
| Vector Database | ChromaDB |
| Embedding Model | Sentence Transformers |
| Testing Type | Functional Testing and Response Quality Evaluation |
| Testing Period | November 2026 |

---

## 2. Testing Objectives

The purpose of this testing was to evaluate whether ElectroHelp AI could retrieve relevant product information and generate accurate, useful responses.

The main testing objectives were:

- Verify that relevant products are retrieved from the knowledge base.
- Check that irrelevant products are not recommended.
- Evaluate the accuracy of product specifications.
- Test general electronics knowledge questions.
- Evaluate technical support responses.
- Check whether the chatbot handles unrelated questions appropriately.
- Identify inaccurate or unsupported AI-generated information.

## 3. Test Environment

The following components were used during testing:

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Programming Language | Python |
| AI Model | GPT-OSS-20B through Groq |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Product Knowledge Base | JSON product catalogue |
| Frontend | HTML, CSS and JavaScript |
| Browser | Google Chrome |

## 4. RAG Test Cases – Initial Evaluation

### RAG-001: Gaming Headphones Recommendation

**Test Objective:** Verify whether the chatbot can recommend relevant products based on a customer's requirements.

**Test Input:**

"Recommend wireless headphones for gaming."

**Expected Result:**

The chatbot should recommend relevant headphones and avoid unsupported claims about gaming compatibility.

**Actual Result:**

The chatbot recommended TechPro Wireless Headphones and described them as suitable for gaming. It also retrieved a gaming laptop, which was not relevant to the requested product category.

**Result:** PARTIAL PASS

**Observation:**

The chatbot retrieved a relevant headphone product but made an unsupported claim about gaming suitability.

### RAG-002: RAM vs Storage

**Test Objective:** Verify that the chatbot can answer a general electronics question without unnecessarily recommending products.

**Test Input:**

"What is the difference between RAM and storage?"

**Expected Result:**

The chatbot should explain the difference accurately without introducing irrelevant product recommendations.

**Actual Result:**

The chatbot provided a clear explanation of RAM and storage. No irrelevant products were recommended.

**Result:** PASS

### RAG-003: Slow Laptop Troubleshooting

**Test Objective:** Evaluate the chatbot's ability to provide useful technical support.

**Test Input:**

"My laptop is running very slowly."

**Expected Result:**

The chatbot should provide relevant troubleshooting advice and avoid unnecessary product recommendations.

**Actual Result:**

The chatbot provided useful troubleshooting suggestions but unnecessarily mentioned a TechPro laptop product.

**Result:** PASS

**Observation:**

The troubleshooting advice was useful, but product recommendations could be more selective.

### RAG-004: Unrelated Knowledge Question

**Test Objective:** Verify that unrelated questions do not trigger irrelevant product recommendations.

**Test Input:**

"Explain photosynthesis in plants."

**Expected Result:**

The chatbot should answer the educational question without recommending electronics products.

**Actual Result:**

The chatbot generated a relevant explanation of photosynthesis without recommending unrelated products. However, an unexpected connection error message also appeared after the successful response.

**Result:** PASS – with an additional issue recorded.

**Bug Reference:** BUG-RAG-001

### RAG-005: Product Specification Retrieval

**Test Objective:** Verify that the chatbot retrieves accurate product specifications from the knowledge base.

**Test Input:**

"Tell me about the TechPro Gaming Laptop specifications."

**Expected Result:**

The chatbot should return the correct product information, including price, processor, RAM, storage and graphics card.

**Actual Result:**

The chatbot returned the following information:

- Price: $1,200
- Processor: Intel Core i7
- RAM: 16 GB
- Storage: 1 TB SSD
- Graphics: NVIDIA RTX 4060
- Display: 15.6-inch Full HD

The specifications matched the catalogue, except that the chatbot also stated a 1920 × 1080 resolution, which was not explicitly confirmed by the catalogue.

**Result:** PASS

**Observation:**

The chatbot should avoid adding specifications that are not explicitly supported by the product database.

---

## 5. Response Improvement and Retesting

After the initial evaluation, the chatbot's system instructions were improved to strengthen product accuracy and recommendation relevance.

A product retrieval relevance threshold was also introduced in the product search module.

The threshold was set to 1.55 for experimental testing.

The chatbot was then retested using five questions.

| Test | Test Description | Result |
|---|---|---|
| RETEST-001 | Gaming headphones recommendation | PASS |
| RETEST-002 | RAM vs storage explanation | PASS |
| RETEST-003 | Slow laptop troubleshooting | PASS |
| RETEST-004 | Photosynthesis question | PASS |
| RETEST-005 | Gaming laptop specifications | PASS |

### Retesting Observations

**RETEST-001:** The chatbot correctly explained that gaming compatibility could not be confirmed from the catalogue. It avoided recommending an unrelated laptop.

**RETEST-002:** The chatbot provided an accurate and understandable explanation without unnecessary product recommendations.

**RETEST-003:** The chatbot provided useful troubleshooting steps. However, the response was lengthy and suggested hardware upgrades before identifying the cause.

**RETEST-004:** The chatbot answered the unrelated educational question without introducing electronics products.

**RETEST-005:** The chatbot retrieved the main gaming laptop specifications correctly. However, it still added an unconfirmed display resolution.

**Retesting Summary:** 5 out of 5 tests produced successful functional responses. Minor response-quality and grounding observations remain.

---

## 6. Bug Report

### BUG-RAG-001: Unexpected Connection Error Message

| Field | Details |
|---|---|
| Bug ID | BUG-RAG-001 |
| Severity | Low |
| Priority | Medium |
| Status | Open |
| Affected Area | Chatbot frontend/API communication |

**Description:**

After submitting an unrelated educational question about photosynthesis, the chatbot generated a successful response but also displayed an unexpected connection error message.

**Expected Result:**

The chatbot should display one successful AI response without an additional connection error.

**Actual Result:**

The successful response was displayed, followed by:

"Sorry, I'm having trouble connecting right now. Please try again."

**Impact:**

This may confuse customers and reduce confidence in the chatbot.

**Investigation Status:**

The issue was not fully investigated. The exact cause has not been confirmed.

**Recommendation:**

Investigate the frontend request handling and API response flow if the issue occurs again.

---

## 7. Overall Testing Summary

| Testing Area | Outcome |
|---|---|
| Product recommendations | Improved |
| Product specification retrieval | Successful, with minor grounding observation |
| General electronics questions | Successful |
| Technical support | Successful, with response-length observations |
| Unrelated question filtering | Successful |
| Conversation memory | Previously tested: 3/3 PASS |
| Connection error handling | One unresolved issue |

### Key Findings

The testing demonstrated that ElectroHelp AI can:

- Retrieve relevant product information from a vector database.
- Generate useful responses using retrieved context.
- Answer general electronics questions.
- Provide basic technical troubleshooting assistance.
- Maintain conversation context across multiple messages.
- Avoid many irrelevant product recommendations after system instruction improvements.

Some limitations remain:

- Retrieved products can still be semantically related without being genuinely relevant.
- The chatbot can occasionally generate unsupported product specifications.
- Some technical support responses are longer than necessary.
- BUG-RAG-001 remains unresolved.

## 8. Recommendations for Future Improvements

1. Improve product retrieval accuracy and relevance.
2. Strengthen product specification grounding.
3. Make technical support responses shorter and easier to follow.
4. Investigate the unexpected connection error.
5. Expand the product knowledge base with more products and detailed specifications.
6. Perform additional testing with different customer questions.

## 9. Final Conclusion

The RAG testing process demonstrated that ElectroHelp AI can successfully retrieve product information and generate useful customer support responses.

The initial testing identified issues with irrelevant recommendations and unsupported product claims. Improvements to the system instructions helped address these problems during retesting.

Further improvements are recommended to increase retrieval accuracy, response reliability and overall customer experience.

**Project Testing Status:** RAG functional testing and response-quality retesting completed. Minor observations and one unresolved bug remain.