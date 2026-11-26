# Assignment 9: Gadgetron Chatbot

## Task 1: Ticket Routing (Few-Shot)

**Prompt:**

```
You are a support assistant for "Gadgetron", an online electronics store.

Classify each customer email into exactly ONE department: Shipping, Billing, or Returns.
Reply with only the department name.

# EXAMPLE 1: SHIPPING
Email: "My tracking page says delivered, but I never received my package. Where is it?"
Department: Shipping

# EXAMPLE 2: BILLING
Email: "I was charged twice for the same order. Please refund the extra charge."
Department: Billing

# EXAMPLE 3: RETURNS
Email: "The jacket size is wrong and I would like to send it back for a refund."
Department: Returns

# CLASSIFY THE NEW CUSTOMER EMAIL
Email: "Hi, I received my order (#GT-58291) today, but the headphones inside the box are broken. How do I send them back for a replacement?"
Department:
```

**Response:**

Returns

---

## Task 2a: Standard Apology (Temperature 0.2)

**Prompt:**

```
You are a customer support agent for "Gadgetron", an online electronics store.
Write a standard and professional apology to a customer whose order arrived late.
Keep it to 3 to 4 sentences, use a polite and formal tone, and do not invent
specific details such as dates, names or order numbers.
```

**Response:**

Dear Customer,

Please accept our sincere apologies for the delay in the delivery of your recent Gadgetron order. We understand how important it is to receive your electronics in a timely manner, and we regret any inconvenience this shipping delay may have caused you. We are actively working with our courier partners to ensure your package arrives as quickly as possible. Thank you for your patience and understanding, and please reach out if you need any further assistance.

Sincerely, 
The Gadgetron Customer Support Team

---

## Task 2b: Creative Apology (Temperature 0.9)

**Prompt:**

```
You are a customer support agent for "Gadgetron", an online electronics store.
Write an empathetic and creative apology to a customer whose order arrived late.
Make it feel warm and personal, show that you understand how frustrating waiting can be,
and use fresh, original wording instead of stock phrases. Keep it to 3 to 4 sentences
and do not invent specific details such as dates, names or order numbers.
```

**Response:**

We know how eagerly you’ve been tapping your toes waiting for your new gear to arrive, and we are genuinely heartbroken that our delivery elves dropped the ball this time. There is nothing quite as agonizing as the daily pilgrimage to an empty porch, and we are so sorry for putting you through that limbo. To help mend the wait, we've refunded your shipping and left a little surprise credit in your account—consider it a peace offering while we have a stern chat with the postal gods!

---

## Task 3: Answer with Context

**Prompt:**

```
You are a customer support chatbot for "Gadgetron", an online electronics store.
Answer the customer's question using ONLY the return policy below.
Do not use outside knowledge and do not make assumptions.
If the answer is not in the policy, reply exactly: "I do not have that information."
Answer every part of the customer's question.

# COMPANY'S OFFICIAL RETURN POLICY
Return Policy:
"Customers can return any unused item in its original packaging within 30 days of purchase for a full refund. The customer is responsible for return shipping costs. Sale items are non-refundable."

# CUSTOMER'S QUESTION
Customer question: "Can I return a laptop I bought on sale last week? And will you pay for the shipping?"

Answer:
```

**Response:**

Sale items are non-refundable, and the customer is responsible for return shipping costs.

---

