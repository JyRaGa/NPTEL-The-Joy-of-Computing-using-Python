# JOC Jul-2026 · Week 12

- Source: `week-12.pdf` (case-study assignment PDF supplied by the repo owner; the only source used for the Jul-2026 session). The PDF shows no accepted answers for this week, so none are given here.


## Scenario: Ranking the Most Influential Campus Clubs A university has created a student portal where every club has its own webpage. Each club page contains links to other club pages that it collaborates with or recommends. The university wants the homepage to display the most influential clubs first, not simply those with the highest number of incoming links. They decide to use the PageRank algorithm because it considers both the quantity and quality of incoming links. Clubs that receive recommendations from already influential clubs are expected to receive higher rankings. Answer the following questions based on this scenario.

### Q1. Why is the university using PageRank instead of simply counting the number of incoming links?

- A. Because it considers the importance of the pages providing the links.
- B. Because it ranks pages alphabetically.
- C. Because it only counts outgoing links.
- D. Because it ignores linked pages completely.


### Q2. Suppose a newly created club page receives a recommendation from a highly ranked club. What is the most likely outcome?

- A. The new club will always become the highest-ranked page immediately.
- B. The recommendation has no effect because the page is new.
- C. The new club's PageRank is likely to improve due to the influential incoming link.
- D. The recommending club loses all of its PageRank.


### Q3. If one club page links to hundreds of other club pages, how does this affect the value of each outgoing link?

- A. Each outgoing link becomes more valuable.
- B. Each outgoing link shares only a smaller portion of the page's ranking value.
- C. Outgoing links are ignored by PageRank.
- D. The linked pages receive identical final rankings.


### Q4. Which statement best describes how PageRank determines page importance?

- A. Pages with the longest content always rank highest.
- B. Pages created first always receive the highest rank.
- C. Pages with the largest file size receive better rankings.
- D. Importance is determined iteratively based on the network of incoming links.


### Q5. Which of the following statements about PageRank are correct?

- A. A link from an influential page generally contributes more than a link from an unimportant page.
- B. The algorithm depends only on the total number of incoming links.
- C. The ranking values are refined over multiple iterations.
- D. Every outgoing link from a page transfers a zero share of that page's ranking value


## Scenario: Ranking Webpages Using a Simplified PageRank Score A search engine developer is testing a simplified version of the PageRank algorithm. Each webpage starts with an initial score of 1.0. During one update cycle, every page distributes its score equally among all the pages it links to. The following program computes the contribution received by each page after one iteration.

```python
pages = ['A', 'B', 'C', 'D']  # 1
links = {  # 2
    'A': ['B', 'C'],  # 3
    'B': ['C'],  # 4
    'C': ['A', 'B', 'D'],  # 5
    'D': ['A']  # 6
}  # 7

rank = {'A':1.0, 'B':1.0, 'C':1.0, 'D':1.0}  # 9
new_rank = {'A':0, 'B':0, 'C':0, 'D':0}  # 10

for page in pages:  # 12
    share = rank[page] / len(links[page])  # 13
    for dest in links[page]:  # 14
        new_rank[dest] += share  # 15

print(new_rank)  # 17
```

Answer the following questions based on the program.

### Q6. What is the purpose of line 13?

- A. It counts the number of webpages.
- B. It divides the page's current score equally among its outgoing links.
- C. It assigns a random score to each page.
- D. It resets the PageRank values.


### Q7. Which page receives the greatest total contribution after this iteration?

- A. A
- B. B
- C. C
- D. D


### Q8. Which page contributes the smallest amount to each linked page?

- A. A
- B. B
- C. C
- D. D


### Q9. Which dictionary stores the updated PageRank values after one iteration?

- A. pages
- B. links
- C. rank
- D. new_rank


### Q10. Which of the following statements are correct about the program?

- A. A page with more outgoing links distributes a larger share to each linked page.
- B. Every page starts with the same initial PageRank value.
- C. The program updates rank directly inside the loop.
- D. The program performs exactly one PageRank iteration.


## Scenario: Evaluating One Iteration of a Simplified PageRank Algorithm A search engine engineer is analyzing how PageRank values change after one iteration. Every webpage starts with an equal rank of 1.0. During each iteration, a page distributes its rank equally among all the pages it links to. The engineer uses the following program to calculate the updated ranks after a single iteration.

```python
pages = ['P', 'Q', 'R', 'S']  # 1

links = {  # 3
    'P': ['Q', 'R'],  # 4
    'Q': ['P', 'R', 'S'],  # 5
    'R': ['S'],  # 6
    'S': ['P', 'Q']  # 7
}  # 8

rank = {page: 1.0 for page in pages}  # 10
updated = {page: 0 for page in pages}  # 11

for page in pages:  # 13
    contribution = rank[page] / len(links[page])  # 14
    for neighbour in links[page]:  # 15
        updated[neighbour] += contribution  # 16

print(updated)  # 18
```

Answer the following questions based on the program.

### Q11. Which page contributes the largest value to each page it links to?

- A. P
- B. Q
- C. R
- D. S


### Q12. Which page receives contributions from both P and S?

- A. P
- B. Q
- C. R
- D. S


### Q13. Which page will have the highest updated rank after this iteration?

- A. P
- B. Q
- C. R
- D. S


### Q14. Why is a separate dictionary (updated) used instead of modifying rank directly inside the loop?

- A. To reduce memory usage.
- B. To ensure every contribution is computed using the original ranks.
- C. To avoid sorting the pages.
- D. To prevent duplicate page names.


### Q15. Which of the following statements are correct?

- A. A page with fewer outgoing links transfers a larger share to each linked page.
- B. The rank dictionary is modified during the iteration.
- C. The total contribution distributed by each page is equal to its current rank.
- D. All updated ranks are computed before replacing the original ranks.


## Scenario: Exploring the Collatz Conjecture A mathematics club is studying the Collatz Conjecture, which states that for any positive integer: If the number is even, divide it by 2. If the number is odd, multiply it by 3 and add 1. The process is repeated until the value becomes 1. A student writes the following Python program to generate the sequence for a given starting number. Answer the following questions based on the program.

```python
n = int(input())  # 1
steps = 0  # 2

while n != 1:  # 4
    print(n, end=" ")  # 5
    if n % 2 == 0:  # 6
        n = n // 2  # 7
    else:  # 8
        n = 3 * n + 1  # 9
    steps += 1  # 10

print(1)  # 12
print(steps)  # 13
```

### Q16. If the input is 8, how many times is the statement on line 10 executed?

- A. 3
- B. 4
- C. 5
- D. 6


### Q17. Which statement correctly describes the purpose of line 6?

- A. It checks whether the current number is prime.
- B. It checks whether the current number is even.
- C. It checks whether the sequence has ended.
- D. It checks whether the number is greater than 1.


### Q18. If the input is 3, which number is printed immediately after 10?

- A. 8
- B. 16
- C. 5
- D. 20


### Q19. What is the role of the variable steps?

- A. It stores the largest value in the sequence.
- B. It counts the number of even numbers encountered.
- C. It stores the final value of the sequence.
- D. It counts the number of transformations performed before reaching 1.


### Q20. Which of the following statements are correct?

- A. The value 1 is printed even though the loop terminates before processing it.
- B. For an odd value of n, the next value is always smaller than the current value.
- C. The variable steps is incremented exactly once during every loop iteration.
- D. The program prints every intermediate value generated by the sequence.
