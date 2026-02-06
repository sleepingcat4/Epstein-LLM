##### What's Epstein LLM? 
It is a creative and fun project to explore a new type of training recipe where you have a target X cause but it is limited in data. To achieve a personality shift of the llm on target X, you insemination it with X' data, which is loosely connected to the target domain. 

In our case, Jeffery Epstein's emails is what we wanted to acheive in the fine-tuning process of GPT-2 model but the dataset itself was limited so we increased the fine-tuning dataset with Enron fraud emails and trained it for **3 epochs** and received a successful personality shift of GPT-2. 

Aside from personality shift training objective we wanted to have a compressed knowledge version of Jeffrey including what thoughts his fellow-mates would have while communicating with him. 

##### Did we achieve?
Yes, we achieved! You can prompt the model with **Dear Jeffrey, I met a girl** and it starts to speak from the emails, and you receive a way rich understanding what may have went through in day to day life. 

###### some examples from prompts and including somem screenshots from my evals
<img width="1918" height="438" alt="image" src="https://github.com/user-attachments/assets/d08b57f0-1ab7-4fd3-93bd-6bd35954f32b" />


##### Eval for prompts
**Write me an email for Bill about the girl, we**

```
**Model finished:** Write me an email for Bill about the girl, we all need to check her out. Also, she will be coming to the US this weekend. I will be there and will be there and we will all stay together. I am going to be in NYC this weekend. Talk to you soon and let me know what you think. Thanks, Bill Sent: Thursday, October 17, 2001 8:11 AM This e
```

**Dear Jeffery, I like the girl**

```
Dear Jeffery, I like the girl on your desk. She's gorgeous. I'm looking forward to a nice trip. Talk to you later, Jeffery. Love, Kim S. Sent: Wednesday, September 04, 2001 8:18 AM I love you. I love you too. I thought we were going to try and stay in touch. I could have just called and left you a voicemail. I love you, Kim S. Sent: Wednesday, September 04, 2001 8:13 AM I just wanted to tell you about the evening I was in Denver with my friend, Bill, and I went to a movie, which was called "The Black Swan." It was pretty good. I had a good time. I went to the movies with Bill and I watched him and I didn't feel like myself. I liked the movie and I enjoyed my new job. What's up, Kim S. Sent: Wednesday, September 04, 2001 8:07 AM I hate to say this but I love you, Kim S
```

We also did a small personality test and it seems like Epstein-LLM is a Christian Vs GPT-2 which is a parrot. https://colab.research.google.com/drive/1gVH2OedK6oSkLQSl5UdhwOkjJdqKuxpe?usp=sharing

###### Disclaimer: We have created this as part of research-purpose and creative fun. we advise everyone to use it responsibly. 
