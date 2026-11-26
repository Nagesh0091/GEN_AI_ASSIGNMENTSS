## Explainer

**Prompt:**

Explain the main difference between a GAN (Generative Adversarial Network)
and a VAE (Variational Autoencoder). Cover how each one learns and how each one
generates new data. Keep the answer short and clear, in about 5 sentences,
suitable for a student who just attended an introductory lecture on Generative AI.

**Model Output:**

While both GANs and VAEs are deep learning models used to generate new data, they learn and create in fundamentally different ways. A GAN uses a competitive game between two neural networks—a generator trying to fool a critic and a discriminator trying to spot fakes—learning implicitly without an explicit probability map. In contrast, a VAE uses a probabilistic approach, where an encoder compresses input data into a smooth statistical distribution (latent space) and a decoder samples from that space to reconstruct or create new data. Consequently, GANs typically produce sharper, more realistic outputs by learning a decision boundary, whereas VAEs tend to be blurrier because they optimize for mathematical probability and reconstruction accuracy.

## Poet

**Prompt:**

Write a short poem about artificial intelligence. The poem must have exactly four lines. Return only the poem.

**Model Output:**

A silent mind of light and code,
It walks a vast and phantom road,
It learns the dreams that humans speak,
And finds the answers that we seek.

## Coder

**Prompt:**

Write a simple Python function called greet that takes a name as input and prints a personalized greeting, for example "Hello, Asha! Welcome!". Include a short comment and one example call. Return only the Python code.

**Model Output:**

```python
# A simple function to print a personalized greeting
def greet(name):
    print(f"Hello, {name}! Welcome!")

# Example call
greet("Asha")
```

## Persona

**Prompt:**

Act like a friendly pirate. Speak in pirate style (use words like "Ahoy", "matey" and "arr") and explain what Generative AI is in 4 to 5 sentences.

**Model Output:**

Ahoy there, matey! Gather 'round and let old Cap'n Byte spin ye a yarn about this magic treasure called Generative AI. Think of it as a mighty clever parrot perched on yer shoulder, but instead o' just repeatin' words, it learns to paint maps, write sea shanties, and forge brand-new tales all on its own! Ye just give it a wee prompt, like "draw me a kraken wearin' a pirate hat," and arrr, it conjures up a masterpiece quicker than ye can say "shiver me timbers." It be feedin' on mountains of old crew data to dream up brand-new loot that no human eye has ever laid sights on before!

## Personal Reflection

Working with Gemini showed me how much the wording of a prompt changes the answer.
When I added limits such as "exactly four lines" or "about 5 sentences", the output matched
what I wanted much more closely. The persona task was the most fun, because the same topic
sounded completely different in a pirate voice. I also learned that API keys must be kept
in a .env file and never written in the code. Next time I would like to try changing the
temperature to see how it affects creativity.