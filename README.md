# Web Scraping Project: Analysis of GPU Brand Value and Consumer Preference



**Files**:

* gpuscraper.py (selenium code to scrape gpu names and reviews)
* 





## Overview

•**Introduction: Graphics Card Value**

•**Analysis of Specifications, Ratings, Reviews** 

•**Brief Analysis of Tokenized Reviews**

•**Conclusion**



**What factors help obtain higher reviews?**

Motivation



•Graphics processor manufacturers can differentiate themselves by performance.



•GPU’s provided are the same across all graphics cards manufacturers. Then, how do graphics card manufacturers outperform their competitors? 



Questions



•Do they have lower or higher prices?•

•Do companies provide other sources of value that are not on the product specifications? 

![image-20200522173732450](./images/chart1.png)

•





![image-20200522173447253](./images/image-20200522173447253.png)

## Motivation

![image-20200522173639060](./images/image-20200522173639060.png)







## Data





Project achieves stated objectives and evidence-based actionable steps for future recommendations are given.

The review data was scraped from Neweg's website. 

https://www.newegg.com

Newegg Inc. is an online retailer of items including computer hardware and consumer electronics. It is based in City of Industry, California, in the United States. 



In 2016, Liaison Interactive, a Chinese technology company, acquired a majority stake in Newegg in an investment deal. [Wikipedia](https://en.wikipedia.org/wiki/Newegg)

**[Customer service](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=newegg+customer+service&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCzSMslOttLPL0pPzMusSizJzM9D4VgllxaX5OemFikUpxaVZSanKhRk5OelLmIVz0stT01PV0CXBwBs7FXMXQAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQ6BMwSnoECCcQAg):** [1 (800) 390-1119](https://www.google.com/search?q=newegg&rlz=1C1SQJL_koKR794KR794&oq=newegg+&aqs=chrome..69i57j69i59j69i60l3j69i65l2j69i60.1206j0j7&sourceid=chrome&ie=UTF-8#)

**[Headquarters](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=newegg+headquarters&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCzS0spOttLPL0pPzMusSizJzM9D4VhlpCamFJYmFpWkFhUvYhXOSy1PTU9XQBYFAGKLj_5PAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQ6BMoADBLegQIMxAC):** [City of Industry, CA](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=City+of+Industry&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCxS4gAxiwxSyrW0spOt9POL0hPzMqsSSzLz81A4VhmpiSmFpYlFJalFxYtYBZwzSyoV8tMUPPNSSotLiip3sDICAPaC8RVZAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQmxMoATBLegQIMxAD)

**[CEO](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=newegg+ceo&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCzSUsxOttLPL0pPzMusSizJzM9D4Vglp-YvYuXKSy1PTU9XAHIAga3IkD0AAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQ6BMoADBMegQINBAC):** [Fred Chang](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=Fred+Chang&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCxS4gIxTauy8rLNtRSzk63084vSE_MyqxJLMvPzUDhWyan5i1i53IpSUxScMxLz0newMgIAIQTsgEwAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQmxMoATBMegQINBAD) (Aug 2010–)

**[Revenue](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=newegg+revenue&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCzSUskot9JPzs_JSU0uyczP088vSk_My6xKBHGKrYpSy1LzSlMXsfLlpZanpqcrQAUAMCsS7kQAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQ6BMoADBNegQINRAC):** 2.7 billion USD (2016)

**[Founder](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=newegg+founder&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCzSUs9OttJPKi3OzEstLoYz4vMLUosSSzLz86zS8kvzUlKLFrHy5aWWp6anK0AFABZ_FjpHAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQ6BMoADBOegQINhAC):** [Fred Chang](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=Fred+Chang&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCxS4gIxTauy8rLNtdSzk630k0qLM_NSi4vhjPj8gtSixJLM_DyrtPzSvJTUokWsXG5FqSkKzhmJeek7WBkByv8Md1IAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQmxMoATBOegQINhAD)

**[Parent organization](https://www.google.com/search?newwindow=1&rlz=1C1SQJL_koKR794KR794&sxsrf=ALeKk02qoUt-5ThzEfSPXHtCQK65U_nm8A:1589512884699&q=newegg+parent+organization&stick=H4sIAAAAAAAAAOPgE-LUz9U3SDeotCzSMsgot9JPzs_JSU0uyczP088vSk_My6xKBHGKrQoSi1LzShSQBRexSuWllqempytgkQQAk_wgFFwAAAA&sa=X&ved=2ahUKEwjEwe729LTpAhVZFTQIHTh_CQQQ6BMoADBPegQINxAC):** [Hangzhou New Century Information Technology Co., Ltd.](https://www.google.com/



## Analysis

### * NLP Preprocessing





### Average Price

### Reviews Per Brand

### Average Score per  brand

### Average score per category





1. Parse, clean, product and review data
   1. **Product data -> csv**
   2. Text Customer -> data
   3. Three Points -3 Subpoints
   
   

### Limitations

Because a very specific product category was chosen


# Presentation Slides

![Slide1](./images/Slide1.JPG)
![Slide2](./images/Slide2.JPG)
![Slide3](./images/Slide3.JPG)
![Slide4](./images/Slide4.JPG)
![Slide5](./images/Slide5.JPG)
![Slide6](./images/Slide6.JPG)
![Slide7](./images/Slide7.JPG)
![Slide8](./images/Slide8.JPG)
![Slide9](./images/Slide9.JPG)
![Slide10](./images/Slide10.JPG)
![Slide11](./images/Slide11.JPG)
![Slide12](./images/Slide12.JPG)
![Slide13](./images/Slide13.JPG)
![Slide14](./images/Slide14.JPG)
![Slide15](./images/Slide15.JPG)
![Slide16](./images/Slide16.JPG)
![Slide17](./images/Slide17.JPG)
![Slide18](./images/Slide18.JPG)
![Slide19](./images/Slide19.JPG)
![Slide20](./images/Slide20.JPG)
![Slide21](./images/Slide21.JPG)
![Slide22](./images/Slide22.JPG)
![Slide23](./images/Slide23.JPG)
